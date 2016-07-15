import serial
from binascii import hexlify, unhexlify
from time import sleep
import json
import os
import time
import logging

logging.basicConfig(filename='log.log', level=logging.DEBUG,format='%(asctime)-15s %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__) 

class SerialAPI(object):

	

	def __init__(self):
		if os.path.isfile('config.json'):
			with open('config.json','r') as f:
				self.elements = json.load(f)
			self.port = self.elements['port']
			self.baudrate = self.elements['baudrate']
		else:
			self.port = "COM1"
			self.baudrate = "9600"		

	def open(self):
		self.ser = serial.Serial(self.port, self.baudrate,timeout=0)

	def send(self, data):
		data = self.hex_to_binary(self.remove_space(data))
		self.ser.write(data)

	def recieve(self,timeout=15):
		start = int(time.time())
		run_time = 0
		while True:
			data = self.ser.read(1)
			if data == b'':
				end = int(time.time())
				run_time = end - start
				if run_time>timeout:
					break
				else:
					continue
			while True:
			    n = self.ser.inWaiting()

			    if n > 0:
			        data = "%s%s" % (data, self.ser.read(n))
			        sleep(0.3) #  add a internal in case can't recieve data
			    else:
			        quit = True
			        break

			if quit:
			    break
		if run_time>timeout:
			return "Recieve data timeout!!!"
		else:
			return self.binary_to_hex(data)

	def hex_to_binary(self, data):
		return b''.join([unhexlify(data[i:i+2]) for i in range(0, len(data), 2)])

	def binary_to_hex(self,data):	
		fillter = "bx\'\\"
		# print(data)
		hex_data =  [c for c in data if str(c) not in fillter]
		#remove the header 02 and ender 03
		data = [hexlify(bytearray(c,'utf-8')).decode() for c in hex_data[2:-2]]
		data.insert(0, '02')
		data.insert(len(data),'03')
		return ' '.join([byte for byte in data])

	def remove_space(self, data):
		return data.replace(" ","")

	def close(self):
		self.ser.close()

	def delay_send(self, command, sleep_time):
		# print "send command:",command
		# print "delay time:",sleep_time
		self.send(command)
		sleep(int(sleep_time))

class SerialDelayTest(object):

	logging.basicConfig(filename='log.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

	def delay_send_test_by_custom(self, serial, run_time=1):
		path = 'delay.json'
		result = []
		if os.path.isfile(path):
			with open(path,'r') as f:
				data = json.load(f)
			# read run time from configuration
			if run_time == 1 and data['runtime'] > 0:
				run_time = int(data['runtime'])
			for i in range(run_time):
				record = 1
				for commands in data:
					run_result = {}
					instruction = ""
					for send_data in commands['commands']:
						serial.delay_send(send_data['command'], send_data['delay'])
						instruction += send_data['command']
						instruction += " "
					recieve_data = serial.recieve(5)
					expect = commands['expect']
					run_result['result'] = recieve_data
					run_result['send'] = instruction
					run_result['expect'] = expect
					run_result['record_number'] = record
					self.print_result(record, instruction, recieve_data, expect)
					record += 1
					result.append(run_result)
		else:
			print("Can't load test case file.")
			logger.warning("Can't load test case file.")
		return result

	def delay_send_test_by_byte(self, serial, run_time=1):
		path = 'delay_by_byte.json'
		result = []
		if os.path.isfile(path):
			with open(path, 'r') as f:
				data = json.load(f)
			if run_time == 1 and int(data['runtime']) > 0:
				run_time = int(data['runtime'])
			for i in range(run_time):
				interval = int(data['interval'])
				delay = int(data['delay'])
				record = 1
				for send_data in data['commands']:
					run_result = {}
					
					command_list = send_data['command'].split()
					for index in range(0, len(command_list), interval):
						instruction  = command_list[index:index+interval] if (index+interval) < len(command_list) else command_list[index:]
						instruction = ' '.join(instruction)
						print("sending:",instruction)
						serial.delay_send(instruction, delay)
					recieve_data = serial.recieve(5)
					expect = send_data['expect']
					run_result['result'] = recieve_data
					run_result['send'] = send_data['command']
					run_result['expect'] = expect
					run_result['record_number'] = record
					self.print_result(record, send_data['command'], recieve_data, expect)
					record += 1
					result.append(run_result)
		else:
			print("Can't load test case file.")
			logger.warning("Can't load test case file.")
		return result


	def print_result(self,record_number, send, recieve, expect):
		print(50 * '*')
		print("No.   : " , record_number)
		print("send  : " , send)
		print("result: " , recieve)
		print("expect: " , expect)
		print(50 * '*'   , '\n')
		logger.info(50 * '*')
		logger.info("No.   :%s " , record_number)
		logger.info("send  :%s " , send)
		logger.info("result:%s " , recieve)
		logger.info("expect:%s " , expect)
		logger.info(50 * '*')

# example to run:
s1 = SerialAPI()
s1.open()
# s.send('0200310000009303')
# print("recieve",s.recieve(3))
# s.close()
s = SerialDelayTest()
s.delay_send_test_by_byte(s1)
