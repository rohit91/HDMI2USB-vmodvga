import time
import serial
s = serial.Serial("COM60")
for i in range(10):
	s.write('[')
	time.sleep(0.01)
	s.write('w')
	time.sleep(0.01)
	s.write(']')
	time.sleep(0.01)
	s.write(chr(0xaa))
	time.sleep(0.01)
	s.write(' ')
	time.sleep(0.01)
	time.sleep(0.2)
	s.write('[')
	time.sleep(0.01)
	s.write('w')
	time.sleep(0.01)
	s.write(']')
	time.sleep(0.01)
	s.write(chr(0x55))
	time.sleep(0.01)
	s.write(' ')
    
s.write('[w]' + chr(0xAA) + ' ')
s.write('[w]' + chr(0x55) + ' ')