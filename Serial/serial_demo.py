import serial
from binascii import hexlify, unhexlify
from time import sleep

#setting
port = "COM4"
baudrate=9600
command = '0200310000009303'


#Return the binary data represented by the hexadecimal string 
toHex = lambda hex_data: ''.join([unhexlify(hex_data[i:i+2]) for i in xrange(0, len(hex_data), 2)])

#Return the hexadecimal representation of the binary data
toVisualHex = lambda hex_data: ' '.join([hexlify(c) for c in hex_data]).upper()

with serial.Serial(port,baudrate,timeout=0) as ser:
	ser.write(toHex(command))
	while True:
		data = ser.read(1)
		if data == '':
		    continue
		while True:
		    n = ser.inWaiting()
		    if n > 0:
		        data = "%s%s" % (data, ser.read(n))
		        sleep(0.02) # data is this interval will be merged
		    else:
		        quit = True
		        break
		if quit:
		    break

print toVisualHex(data)
