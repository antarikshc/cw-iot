import socket
import RPi.GPIO as GPIO
from subprocess import call

# GPIO Setting Up
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

# Create a Server Socket and wait for a client to connect
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 6666))
print ("UDPServer Waiting for client on port 6666")

# Define moving functions
def FW():
    GPIO.output(13,True)
    print ("On")
    call(["ls", "-l"])
    
def STOP():
    GPIO.output(13,False)
    print ("Off")
    call(["ls", "-all"])
options = { "0" : FW,
                "3" : STOP,
}
# Recive data from client and decide which function to call
while True:
    dataFromClient, address = server_socket.recvfrom(256)
    dataFromClient = dataFromClient.rstrip()
    #print(dataFromClient.decode())
    options[dataFromClient.decode()]()