from ar400_driver import Ar400Driver
import time

class SignBillDriver(Ar400Driver):
	"""docstring for SignBillDriver"""
	def __init__(self,driver):
		super(SignBillDriver, self).__init__()

		self.driver = driver
		self.sign_bill_keyboard = Ar400Driver.KeybordDriver(self.sign_bill_elements, self.driver)

	def sign(self):
		self.click(self.sign_bill_elements['sign_btn'])
		time.sleep(int(self.sign_bill_elements['sign_time']))

	def next(self):
		return self.click(self.sign_bill_elements['next_btn'])

	def select_bill_type(self):
		return self.click(self.sign_bill_elements['drop_list'])

	def give_up_bill(self):
		return self.click(self.sign_bill_elements['give_up_btn'])

	def confirm_bill(self):
		return self.click(self.sign_bill_elements['confirm_btn'])

	def click(self, reource_id):
		return self.driver.find_element_by_id(resource_id).click()
		
	def finish_sign_bill(self):
		return self.click(self.sign_bill_elements['back_to_mainpage'])	

	def contiune_sign_bill(self):
		return self.click(self.sign_bill_elements['contiune_sign'])	

	def sign_bill(self):
		self.sign()
		self.next()
		self.confirm_bill()
		self.contiune_sign()


a = SignBillDriver("good")
print time.strftime("%Y-%m-%d-%H-%M-%S")
print a.sign()
print time.strftime("%Y-%m-%d-%H-%M-%S")