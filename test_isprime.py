import unittest
import prime

class TestPrime(unittest.TestCase):
    def test_with_known_prime_numbers(self):
        self.assertTrue(prime.isPrime(257))
        self.assertTrue(prime.isPrime(13))
        self.assertTrue(prime.isPrime(4657))
        self.assertTrue(prime.isPrime(23))
        self.assertTrue(prime.isPrime(31))
        self.assertTrue(prime.isPrime(19))
        self.assertTrue(prime.isPrime(19997))
        self.assertTrue(prime.isPrime(199933))
        #self.assertTrue(prime.isPrime(433494437))
        self.assertTrue(prime.isPrime(2))
        self.assertTrue(prime.isPrime(3))
        self.assertTrue(prime.isPrime(5))
        self.assertTrue(prime.isPrime(7))
        self.assertTrue(prime.isPrime(11))
        self.assertTrue(prime.isPrime(17))

    def test_with_known_composite_numbers(self):
        self.assertFalse(prime.isPrime(22))
        self.assertFalse(prime.isPrime(8))
        self.assertFalse(prime.isPrime(21))
        self.assertFalse(prime.isPrime(25))
        self.assertFalse(prime.isPrime(29384753))
        self.assertFalse(prime.isPrime(1))
