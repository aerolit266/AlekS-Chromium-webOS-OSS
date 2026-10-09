import unittest
from tools.browser_lifecycle import check

class LifecycleTests(unittest.TestCase):
    def test_normal_exit(self):
        self.assertEqual(check(["LAUNCH","READY","BACK","CLOSED"]), [])
    def test_fullscreen_then_exit(self):
        self.assertEqual(check(["LAUNCH","READY","ENTER_FULLSCREEN","BACK","BACK","CLOSED"]), [])
    def test_explicit_exit(self):
        self.assertEqual(check(["LAUNCH","READY","EXIT_REQUEST","CLOSED"]), [])
    def test_cannot_close_without_exit_request(self):
        self.assertTrue(check(["LAUNCH","READY","CLOSED"]))
    def test_double_launch(self):
        self.assertTrue(check(["LAUNCH","LAUNCH","READY","EXIT_REQUEST","CLOSED"]))
    def test_missing_ready(self):
        self.assertTrue(check(["LAUNCH","BACK","CLOSED"]))
    def test_unknown_event(self):
        self.assertTrue(check(["LAUNCH","READY","INVALID","EXIT_REQUEST","CLOSED"]))
    def test_empty(self):
        self.assertTrue(check([]))
if __name__ == "__main__":
    unittest.main()
