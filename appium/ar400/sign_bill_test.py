import unittest
from calculator_driver import CalculatorDriver

class CalculatorTest(unittest.TestCase):

	def setUp(self):
		self.calcultor_driver = CalculatorDriver()

	

	def tearDown(self):
		self.calcultor_driver.quit()

if __name__ == '__main__':
    unittest.main()