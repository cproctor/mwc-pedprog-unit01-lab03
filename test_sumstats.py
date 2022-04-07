from unittest import TestCase, main
from sumstats import (
    mean, 
    median, 
    mode,
    variance,
    standard_deviation,
)

class TestMean(TestCase):
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 8, 16, 32, 64]
    c = [1, -2, -2, 3, 3, 3, -4, -4, -4, -4]

    def test_returns_correct_value(self):
        self.assertEqual(mean(self.a), 5)
        self.assertEqual(mean(self.b), 21)
        self.assertEqual(mean(self.c), -1)
         
class TestMedian(TestCase):
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 8, 16, 32, 64]
    c = [1, -2, -2, 3, 3, 3, -4, -4, -4, -4]

    def test_returns_correct_value(self):
        self.assertEqual(median(self.a), 5)
        self.assertEqual(median(self.b), 12)
        self.assertEqual(median(self.c), -2)
         
class TestMode(TestCase):
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 8, 16, 32, 64]
    c = [1, -2, -2, 3, 3, 3, -4, -4, -4, -4]

    def test_returns_correct_value(self):
        self.assertEqual(mode(self.a), 1)
        self.assertEqual(mode(self.b), 2)
        self.assertEqual(mode(self.c), -4)
         
class TestVariance(TestCase):
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 8, 16, 32, 64]
    c = [1, -2, -2, 3, 3, 3, -4, -4, -4, -4]

    def test_returns_correct_value(self):
        self.assertEqual(variance(self.a), 10)
        self.assertEqual(variance(self.b), 562.8)
        self.assertEqual(variance(self.c), 10)
         
class TestStandardDeviation(TestCase):
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 8, 16, 32, 64]
    c = [1, -2, -2, 3, 3, 3, -4, -4, -4, -4]

    def test_returns_correct_value(self):
        self.assertAlmostEqual(standard_deviation(self.a), 3.162, places=2)
        self.assertAlmostEqual(standard_deviation(self.b), 23.723, places=2)
        self.assertAlmostEqual(standard_deviation(self.c), 3.162, places=2)
         
if __name__ == '__main__':
    main()
