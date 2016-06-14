import unittest
from calculator_driver import CalculatorDriver

class CalculatorTest(unittest.TestCase):

	def setUp(self):
		self.calcultor_driver = CalculatorDriver()

	def test_plus_between_integers(self):
		print(10*'---'+"Plus Test"+10*'---')

		#there is not delete button if calcultor has previous result
		self.calcultor_driver.clear_result()

		# excute: 1 + 9999999
		print("Doing: 1 + 9999999 ...")
		self.calcultor_driver.click_one()
		self.calcultor_driver.click_plus()
		self.calcultor_driver.click_nine(7)		
		self.calcultor_driver.click_equal()

		result = self.calcultor_driver.get_result()

		print("Calculator result : " + result)
		print("Right Answer      : " + "10000000")

		self.calcultor_driver.take_screenshot("plus_result")
		self.assertEqual("10000000", result, "Wrong answer")
		

		print(10*'---'+"Finish Plus Test"+10*'---')
		print('\n')

	def test_plus_between_dots(self):
		print(10*'---'+"Dots Plus Test"+10*'---')

		#there is not delete button if calcultor has previous result
		self.calcultor_driver.clear_result()

		# excute: 1 + 9999999
		print("Doing: :1.001 + 9.009")
		self.calcultor_driver.click_one()
		self.calcultor_driver.click_dot()
		self.calcultor_driver.click_zero(2)
		self.calcultor_driver.click_one()

		self.calcultor_driver.click_plus()	
		
		self.calcultor_driver.click_nine()	
		self.calcultor_driver.click_dot()
		self.calcultor_driver.click_zero(2)
		self.calcultor_driver.click_nine()

		self.calcultor_driver.click_equal()

		result = self.calcultor_driver.get_result()

		print("Calculator result : " + result)
		print("Right Answer      : " + "10.01")

		self.calcultor_driver.take_screenshot("dots_plus")
		self.assertEqual("10 point 01", result, "Wrong answer")
		

		print(10*'---'+"Finish Plus Test"+10*'---')
		print('\n')

	def test_pi(self):
		print(10*'---'+"Pi  Test"+10*'---')

		#excute : pi + 1 
		print("Doing: pi +1...")
		self.calcultor_driver.clear_result()
		self.calcultor_driver.enter_advance_panel()
		self.calcultor_driver.click_pi()
		self.calcultor_driver.click_plus()
		self.calcultor_driver.click_one()
		self.calcultor_driver.click_equal()

		result = self.calcultor_driver.get_result()
		
		print("Calculator result : " + result)
		print("Right Answer      : " + "4.14159265")

		self.calcultor_driver.take_screenshot("pi_plus_1")
		self.assertEqual("4 point 14159265", result, "Wrong answer")

		print(23*'---')

		#excute : pi * 2
		print("Doing: pi * 2 ...")
		self.calcultor_driver.clear_result()
		self.calcultor_driver.clear_result()
		self.calcultor_driver.enter_advance_panel()
		self.calcultor_driver.click_pi()
		self.calcultor_driver.click_multipy()
		self.calcultor_driver.click_two()
		self.calcultor_driver.click_equal()
		result = self.calcultor_driver.get_result()

		print("Calculator result : " + result)
		print("Right Answer      : " + "6.28318531")

		self.calcultor_driver.take_screenshot("pi_mul_2")
		self.assertEqual("6 point 28318531", result, "Wrong answer")

		print(10*'---'+"Finish Pi Test"+10*'---')
		print('\n')

	def tearDown(self):
		self.calcultor_driver.quit()

if __name__ == '__main__':
    unittest.main()
