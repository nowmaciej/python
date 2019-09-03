from circle_area import circle_area
from math import pi
import unittest

class testCircleArea(unittest.TestCase):
  def test_area(self):
    #testing for radius >=0
    self.assertAlmostEqual(circle_area(1), pi)
    self.assertAlmostEqual(circle_area(0), 0)
    self.assertAlmostEqual(circle_area(7.6), pi*(7.6**2))

  def test_type(self):
    self.assertRaises(TypeError, circle_area, "agata")
    self.assertRaises(TypeError, circle_area, True)
    self.assertRaises(TypeError, circle_area, 6+2j)

  def test_moreEqualZero(self):
    self.assertRaises(ValueError, circle_area, -10)