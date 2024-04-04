import unittest

from mymod import square, double, add  # importing from local files


class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(10), 100)
        self.assertNotEqual(square(-3), -9)


class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(5), 10)
        self.assertEqual(double(2.2), 4.4)
        self.assertNotEqual(double(6), 18)


class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(0, 0), 0)  # should be 0
        self.assertAlmostEqual(add(2.3, 3.6), 5.9, places=2)
        self.assertEqual(add("hello", "world"), "helloworld")
        self.assertAlmostEqual(add(2.3, 4.3), 6.6, places=2)
        self.assertNotEqual(add(-2, -2), 0)


unittest.main()
