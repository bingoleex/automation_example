from ar_driver import ArDriver
import json
import time

class AntiFakePaperDriver(ArDriver):
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

		def click_single_number(self,index=0):
			try:
				x = int(index)
			except ValueError:
				x = 0
			self.click(self.elements['digit'][x])

		def click_multiple_number(self, numbers):
			for index in numbers:
				self.click_single_number(x)

		def finish_type_number(self):
			return self.click(self.bill_elements['confirm_btn'])

		def previous_number(self):
			return self.click(self.bill_elements['left_btn'])

		def next_number(self):
			return self.click(self.bill_elements['right_btn'])	

		def click(self, reource_id):
			return self.driver.find_element_by_id(resource_id).click()

a = Ar400Driver()