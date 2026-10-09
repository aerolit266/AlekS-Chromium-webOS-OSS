import unittest
from tools.validate_report import validate

GOOD = {
    "device_family": "legacy webOS / ARMv7",
    "webos_version": "6.x",
    "build_id": "research-local",
    "test_type": "playback",
    "environment": "HOST",
    "result": "TESTED_ON_HOST",
    "evidence": "Synthetic stream; successful host-only playback test"
}
class ValidationTests(unittest.TestCase):
    def test_host_pass(self):
        self.assertEqual(validate(GOOD), [])
    def test_tv_requires_tv_environment(self):
        self.assertTrue(validate({**GOOD, "result": "VERIFIED_ON_TV"}))
    def test_private_ip_rejected(self):
        self.assertTrue(validate({**GOOD, "evidence": "Log from 192.168.1.15"}))
    def test_secret_rejected(self):
        self.assertTrue(validate({**GOOD, "token": "not-for-publication"}))
    def test_mac_rejected(self):
        self.assertTrue(validate({**GOOD, "evidence": "aa:bb:cc:dd:ee:ff"}))
    def test_invalid_state(self):
        self.assertTrue(validate({**GOOD, "result": "DONE"}))
    def test_missing_field(self):
        d = dict(GOOD); del d["evidence"]
        self.assertTrue(validate(d))
if __name__ == "__main__":
    unittest.main()
