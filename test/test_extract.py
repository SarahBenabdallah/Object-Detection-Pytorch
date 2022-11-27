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

    def test_get_area_coord(self):
        zones = {"highway_1": [
                [[70, 305], [313, 305], [313, 173], [70, 173]]
                ],
                "highway_2":  [
                [[686, 496], [1051, 496], [1051, 362], [686, 362]]
                ]}
        highway = "highway_1"
        xmin, xmax, ymin, ymax = 70, 313, 173, 305
        self.assertEqual(
                extract.get_area_coord(zones, highway),
                (xmin, xmax, ymin, ymax), f"test failed for testIndex {zones}")

        zones = {"highway_1": [
                [[70, 305], [313, 305], [313, 173], [70, 173]]
                ],
                "highway_2":  [
                [[686, 496], [1051, 496], [1051, 362], [686, 362]]
                ]}
        highway = "highway_2"
        xmin, xmax, ymin, ymax = 686, 1051, 362, 496
        self.assertEqual(
                extract.get_area_coord(zones, highway),
                (xmin, xmax, ymin, ymax), f"test failed for testIndex {zones}")


if __name__ == '__main__':
    unittest.main()
