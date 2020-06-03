import unittest
import fastPowering as f


class testFastPowering(unittest.TestCase):

    @classmethod  # run in the beginning of the test
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):  # run after all tests
        pass

    def setUp(self):  # run before each test
        self.evenSmall = f.fastPowering(2, 4)
        self.evenBig = f.fastPowering(2, 200)
        self.oddSmall = f.fastPowering(3, 4)
        self.oddBig = f.fastPowering(3, 100)
        self.zeroCase = f.fastPowering(12, 0)
        self.oneCase = f.fastPowering(13, 1)
        self.minusCase = f.fastPowering(2, -2)

    def tearDown(self):  # run after each test
        del self.evenSmall
        del self.evenBig
        del self.oddSmall
        del self.oddBig
        del self.zeroCase
        del self.oneCase
        del self.minusCase

    def test_even(self):
        self.assertEqual(self.evenSmall, 16)
        self.assertEqual(self.evenBig, 1606938044258990275541962092341162602522202993782792835301376)

    def test_odd(self):
        self.assertEqual(self.oddSmall, 81)
        self.assertEqual(self.oddBig, 515377520732011331036461129765621272702107522001)

    def test_zero(self):
        self.assertEqual(self.zeroCase, 1)

    def test_one(self):
        self.assertEqual(self.oneCase, 13)

    def test_minus(self):
        self.assertEqual(self.minusCase, 0.25)


if __name__ == '__main__':
    unittest.main()
