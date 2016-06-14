from appium import webdriver
import json
import time

class CalculatorDriver(object):

	def __init__(self):
		# get configuration and app resource
		with open('resource.json','r',encoding='utf8') as f:
			self.elements = json.load(f)
				#config test 
		desired_caps = {}
		desired_caps['platformName'] = self.elements['platform_name']
		desired_caps['platformVersion'] = self.elements['platform_version']
		desired_caps['deviceName'] = self.elements['device_name']
		desired_caps['appPackage'] = self.elements['package_name']
		desired_caps['appActivity'] = self.elements['activity_name']
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

	def click_zero(self, times=1):
		while times >=1:
			self.click(self.elements['digit_0_btn_resource_id'])
			times -= 1

	def click_one(self, times=1):
		while times >=1:
			self.click(self.elements['digit_1_btn_resource_id'])
			times -= 1

	def click_two(self, times=1):
		while times >=1:
			self.click(self.elements['digit_2_btn_resource_id'])
			times -= 1

	def click_three(self, times=1):
		while times >=1:
			self.click(self.elements['digit_3_btn_resource_id'])
			times -= 1

	def click_four(self, times=1):
		while times >=1:
			self.click(self.elements['digit_4_btn_resource_id'])
			times -= 1

	def click_five(self, times=1):
		while times >=1:
			self.click(self.elements['digit_5_btn_resource_id'])
			times -= 1

	def click_six(self, times=1):
		while times >=1:
			self.click(self.elements['digit_6_btn_resource_id'])
			times -= 1

	def click_seven(self, times=1):
		while times >=1:
			self.click(self.elements['digit_7_btn_resource_id'])
			times -= 1

	def click_eight(self, times=1):
		while times >=1:
			self.click(self.elements['digit_8_btn_resource_id'])
			times -= 1

	def click_nine(self, times=1):
		while times >=1:
			self.click(self.elements['digit_9_btn_resource_id'])
			times -= 1

	def click_sin(self):
		return self.click(self.elements['sin_btn_resource_id'])

	def click_cos(self):
		return self.click(self.elements['cos_btn_resource_id'])

	def click_tan(self):
		return self.click(self.elements['tan_btn_resource_id'])

	def click_in(self):
		return self.click(self.elements['in_btn_resource_id'])

	def click_log(self):
		return self.click(self.elements['log_btn_resource_id'])

	def click_factorial(self):
		return self.click(self.elements['factorial_btn_resource_id'])

	def click_pi(self):
		return self.click(self.elements['pi_btn_resource_id'])

	def click_e(self):
		return self.click(self.elements['e_btn_resource_id'])

	def click_power(self):
		return self.click(self.elements['power_btn_resource_id'])

	def click_left_paren(self):
		return self.click(self.elements['left_paren_btn_resource_id'])

	def click_right_paren(self):
		return self.click(self.elements['right_paren_btn_resource_id'])

	def click_sqrt(self):
		return self.click(self.elements['sqrt_paren_btn_resource_id'])

	def click_dot(self):
		return self.click(self.elements['dot_btn_resource_id'])

	def click_plus(self):
		return self.click(self.elements['plus_btn_resource_id'])

	def click_minus(self):
		return self.click(self.elements['minus_btn_resource_id'])

	def click_multipy(self):
		return self.click(self.elements['mul_btn_resource_id'])

	def click_div(self):
		return self.click(self.elements['div_btn_resource_id'])

	def click_equal(self):
		return self.click(self.elements['equal_btn_resource_id'])

	def click_delete(self):
		return self.click(self.elements['delete_btn_resource_id'])

	def click_clear(self):
		return self.click(self.elements['clear_btn_resource_id'])

	def get_result(self):
		return self.driver.find_element_by_class_name(self.elements['result_class']).text

	def enter_advance_panel(self):
		self.click(self.elements['advance_btn_resource_id'])
		self.driver.find_elements_by_xpath("//android.widget.TextView")[1].click()

	def clear_result(self):
		try:
			self.click_delete()
		except:
			self.click_clear()

	def quit(self):
		self.driver.quit()

	def take_screenshot(self, calculate_type='*'):
		return self.driver.get_screenshot_as_file(calculate_type +"-" + time.strftime("%Y-%m-%d-%H-%M-%S")+".png")

	def click(self, resource_id):
		return self.driver.find_element_by_id(resource_id).click()
