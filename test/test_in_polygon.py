import unittest
from src import in_polygon


class TestInPolygon(unittest.TestCase):
    def test_in_polygon(self):
        # if polygon is rectangle
        a = [[70, 305], [313, 305], [313, 173], [70, 173]]
        b = (466, 327)
        self.assertEqual((in_polygon.in_polygon(a, b)), False)
        # if polygon is triangle
        a = [[1350, 500], [1200, 420], [1700, 325]]
        b = (1700, 325)
        self.assertEqual((in_polygon.in_polygon(a, b)), True)
        # if polygon is hexagone
        a = [
            [70, 305], [313, 305], [313, 173],
            [70, 173], [166, 173], [70, 250]]
        b = (466, 327)
        self.assertEqual((in_polygon.in_polygon(a, b)), False)


if __name__ == '__main__':
    unittest.main()
