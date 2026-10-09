import unittest
from tools.analyze_playback import analyze

class PlaybackAnalysisTests(unittest.TestCase):
    def test_valid(self):
        report = analyze({"samples": [
            {"startup_ms": 100, "frame_drops": 0, "seek_ms": 30, "av_drift_ms": -5},
            {"startup_ms": 200, "frame_drops": 2, "seek_ms": 60, "av_drift_ms": 4}
        ]})
        self.assertEqual(report["sample_count"], 2)
        self.assertEqual(report["startup_ms"]["median"], 150)
    def test_empty(self):
        with self.assertRaises(ValueError):
            analyze({"samples": []})
    def test_missing_field(self):
        with self.assertRaises(ValueError):
            analyze({"samples": [{"startup_ms": 10}]})
    def test_negative_startup(self):
        with self.assertRaises(ValueError):
            analyze({"samples": [{"startup_ms": -1, "frame_drops": 0, "seek_ms": 1, "av_drift_ms": 0}]})
    def test_nan(self):
        with self.assertRaises(ValueError):
            analyze({"samples": [{"startup_ms": float("nan"), "frame_drops": 0, "seek_ms": 1, "av_drift_ms": 0}]})
if __name__ == "__main__":
    unittest.main()
