import socket
from time import sleep
import RPi.GPIO as GPIO

# Make TCP connection
TCP_IP = '0.0.0.0' # Look at all IPs
TCP_PORT = 9095
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

door_pin = 12 # That is GPIO 18

def open_door(time):
	GPIO.output(door_pin, True)
	sleep(time)
	GPIO.output(door_pin, False)

def wait_for_user(conn, s):
	conn.recv(BUFFER_SIZE)

def send_message(conn, s, message): # Still Buggy
	html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> ';
	conn.send(html + message)


def close_socket(conn, s):
	conn.close()

def main():

	GPIO.setup(door_pin, GPIO.OUT)

	# Create Socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)	

	print 'Wait for connection'

	
	while True:

		conn, addr = s.accept() 

		wait_for_user(conn, s)
		send_message(conn, s, 'Welcome!')
		
		print "Door Open"
		open_door(5)
		
		close_socket(conn, s)
		print "Door Closed"

if __name__ == "__main__":
    main()