#!/usr/bin/env python

import unittest
from reverse_int import reverse_int

class UnitTests(unittest.TestCase):
   def test_bad_data(self):
      result = reverse_int("a")
      self.assertEqual(result, '0')

   def test_negative(self):
      result = reverse_int(-123)
      self.assertEqual(result, '-321')

   def test_regular_number(self):
      result = reverse_int(123)
      self.assertEqual(result, '321')

   def test_leading_zeros(self):
      result = reverse_int(120)
      self.assertEqual(result, '21')

   def test_for_zero(self):
      result = reverse_int(0)
      self.assertEqual(result, '0')

if __name__ == "__main__":
    unittest.main()
