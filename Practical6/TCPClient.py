import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while 1:
        data = str(input("Enter Data :"))
        # IPADRESS = RPi IP address
        # 6666 = Number Port
        client_socket.sendto(data.encode(), ('192.168.43.237',6666))
        print ("Sending request")

except Exception as ex:
    print (ex)
raw_input()
client_socket.close()