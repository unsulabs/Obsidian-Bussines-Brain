import copy
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from transcripciones_segmentacion import segment_text, validate_partition
from transcripciones_modelo import ModelError


class SegmentTests(unittest.TestCase):
    def test_unicode_exact_reconstruction_and_stability(self):
        data = "á🙂\r\n東京\n".encode()*35
        parts = segment_text(data,"TR-test","V-1",max_core_bytes=13,context_bytes=8)
        self.assertEqual(data,b"".join(data[p["core_start"]:p["core_end"]] for p in parts))
        self.assertEqual([p["segment_id"] for p in parts], [p["segment_id"] for p in segment_text(data,"TR-test","V-1",max_core_bytes=13,context_bytes=8)])
        self.assertEqual(validate_partition(data,parts)["total_core_bytes"],len(data))
        for key,value in (("core_start",1),("text_sha256","0"*64),("ordinal",2)):
            bad=copy.deepcopy(parts); bad[0][key]=value
            with self.assertRaises(ModelError): validate_partition(data,bad)

    def test_binary_and_empty(self):
        for data in (b"",b"\xff"):
            with self.assertRaises(ModelError): segment_text(data,"TR-test","V-1")
