import serial
from binascii import hexlify, unhexlify
from time import sleep
import json
import os
import time

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
		data = self.hex_to_binary(data)
		self.ser.write(data)

	def recieve(self,timeout=15):
		start = int(time.time())
		while True:
			data = self.ser.read(1)
			if data == '':
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
			        sleep(0.02) #  add a internal in case can't recieve data
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
		return ''.join([unhexlify(data[i:i+2]) for i in xrange(0, len(data), 2)])

	def binary_to_hex(self,data):	
		return ' '.join([hexlify(c) for c in data]).upper()

	def close(self):
		self.ser.close()

	def delay_send(self, command, sleep_time):
		print "send command:",command
		print "delay time:",sleep_time
		self.send(command)
		sleep(int(sleep_time))

# example to run:

# s = SerialAPI()
# s.open()
# s.send('0200310000009303')
# print s.recieve()
# s.close()
