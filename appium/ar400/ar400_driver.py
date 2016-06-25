from ar_driver import ArDriver
import json
import time

class Ar400Driver(ArDriver):
	"""docstring for Ar400Driver"""
	def __init__(self):
		with open("ar400_resource.json") as f:
			self.elements = json.load(f)
		self.sign_bill_elements = self.elements['sign_bill']
		self.bill_query_elements = self.elements['bill_query']

		# self.sign_bill_keyboard = Ar400Driver.KeybordDriver(self.elements['bill_query'])
		# self.bill_query_keyboard =  Ar400Driver.KeybordDriver(self.elements['bill_query'])
		# print self.ke

	class KeybordDriver():
		"""docstring for KeybordDriver"""
		def __init__(self, elements, driver):
			self.elements = elements
			self.driver = driver
			# print driver
			# print elements

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

		def finish_type_number(self):
			return self.click(self.bill_elements['confirm_btn'])


		def previous_number(self):
			return self.click(self.bill_elements['left_btn'])

		def next_number(self):
			return self.click(self.bill_elements['right_btn'])	

		def click(self, reource_id):
			return self.driver.find_element_by_id(resource_id).click()