import RPi.GPIO as GPIO
import socket
import sys

from thread import *
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 8
Motor1B = 10
Motor1E = 12

Motor2A = 22
Motor2B = 24
Motor2E = 26

LED = 16

Servo = 18

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(Servo,GPIO.OUT)

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'

print "Now running at: " + socket.gethostbyname(socket.gethostname()) + ":" + str(PORT)
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #infinite loop so that function do not terminate and thread do not end.
    while True:
    
        #Receiving from client
        data = conn.recv(1024)
        
        print data
        if data=='0':

            #Backward
            GPIO.output(Motor1A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
            GPIO.output(Motor1E,GPIO.HIGH)
            
            GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor2B,GPIO.HIGH)
            GPIO.output(Motor2E,GPIO.HIGH)

        elif data=='1':

            #Forward
            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            GPIO.output(Motor1E,GPIO.HIGH)
            
            GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor2B,GPIO.LOW)
            GPIO.output(Motor2E,GPIO.HIGH)
       
        elif data=='2':

             #Right
            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            GPIO.output(Motor1E,GPIO.HIGH)
            
            GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor2B,GPIO.HIGH)
            GPIO.output(Motor2E,GPIO.HIGH)
      
        elif data=='3':

            #Left
            GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor2B,GPIO.LOW)
            GPIO.output(Motor2E,GPIO.HIGH)
            
            GPIO.output(Motor1A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
            GPIO.output(Motor1E,GPIO.HIGH)
        
        elif data=='4':

            #Stop
            GPIO.output(Motor1E,GPIO.LOW)
            GPIO.output(Motor2E,GPIO.LOW)
            
        elif data=='5':

            print 'Camera Up'

        elif data=='6':

            print 'Camera Down'
     
        if not data: 
            break
     

     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread ,(conn,))
 
s.close()
