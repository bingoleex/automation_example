import json
from serial_api import SerialAPI
import unittest
import os

class DelayTest(unittest.TestCase):

	def setUp(self):
		self.serial = SerialAPI()
		self.serial.open()

	# def test_delay_send_data_individual(self):
	# 	if os.path.isfile('delay.json'):
	# 		with open('delay.json','r') as f:
	# 			data = json.load(f)
	# 		record = 0
	# 		for commands in data:
	# 			cmd = ""
	# 			for send_data in commands['commands']:
	# 				self.serial.delay_send(send_data['command'], send_data['delay'])
	# 				cmd += send_data['command']
	# 				cmd += " "
	# 			#set timeout: 5s 
	# 			result = self.serial.recieve(5)
	# 			expect = commands['expect']
	# 			try:
	# 				self.assertEqual(expect, result, "Unexpected.")
	# 			except AssertionError:
	# 				print(50 * '*')
	# 				print("Test Fail.")
	# 				print("run fail record: " , str(record+1))
	# 				print("send  : " , cmd)
	# 				print("result: " ,result)
	# 				print("expect: " , expect)
	# 				print(50 * '*' , '\n')
	# 			record += 1
	# 	else:
	# 		print("Can't not find the data file.")

	def test_delay_send_data_per_byte(self):
		if os.path.isfile('delay_per_time.json'):
			with open('delay_per_time.json','r') as f:
				data = json.load(f)
			for cmd in data['commands']:
				print(cmd)
				print("ok")
	def tearDown(self):
		self.serial.close()

if __name__ == '__main__':
    unittest.main()
