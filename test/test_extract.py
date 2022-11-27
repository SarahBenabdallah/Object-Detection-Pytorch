import unittest
from src import extract


class TestExtract(unittest.TestCase):
    def test_extracthour(self):
        testString = "./input/videos/highway_2_9h.mp4"
        expectedHour = "9"
        self.assertEqual(
                extract.extract_hour(testString),
                expectedHour, f"test failed for testHour {testString}")

        testString = "./input/videos/highway_2_00h.mp4"
        expectedHour = "00"
        self.assertEqual(
                extract.extract_hour(testString),
                expectedHour, f"test failed for testHour {testString}")

        testString = "./input/videos/highway_2_18h.mp4"
        expectedHour = "18"
        self.assertEqual(
                extract.extract_hour(testString),
                expectedHour, f"test failed for testHour {testString}")

    def test_extractindex(self):
        testString = "./input/videos/highway_1_9h.mp4"
        expectedIndex = "1"
        self.assertEqual(
                extract.extract_index(testString),
                expectedIndex, f"test failed for testIndex {testString}")

        testString = "./input/videos/highway_2_00h.mp4"
        expectedIndex = "2"
        self.assertEqual(
                extract.extract_index(testString),
                expectedIndex, f"test failed for testIndex {testString}")

        testString = "./input/videos/highway_10_18h.mp4"
        expectedIndex = "10"
        self.assertEqual(
                extract.extract_index(testString),
                expectedIndex, f"test failed for testIndex {testString}")


if __name__ == '__main__':
    unittest.main()
