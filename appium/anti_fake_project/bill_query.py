from antifake_paper_driver import AntiFakePaperDriver
import time

class BillQueryDriver(AntiFakePaperDriver):

	def __init__(self, driver):
		#load element resource
		super(BillQueryDriver, self).__init__()

		self.driver = driver
		self.bill_query_keyboard = AntiFakePaperDriver.KeybordDriver(self.bill_query_elements, self.driver)

	def next(self):
		self.click(self.bill_query_elements['next_btn'])
		time.sleep(int(self.sign_bill_elements['sign_time']))

	def select_bill_type(self):
		return self.click(self.bill_query_elements['drop_list'])

	def give_up_bill(self):
		return self.click(self.bill_query_elements['give_up_btn'])

	def confirm_bill(self):
		return self.click(self.bill_query_elements['confirm_btn'])

	def click(self, reource_id):
		return self.driver.find_element_by_id(resource_id).click()
		
	def finish_sign_bill(self):
		return self.click(self.bill_query_elements['back_to_mainpage'])	

	def contiune_sign_bill(self):
		return self.click(self.bill_query_elements['contiune_sign'])	

	def bill_query(self):
		self.next()
		self.


# a = BillQueryDriver()