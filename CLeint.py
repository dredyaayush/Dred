import socket,datetime#Module
s = socket.socket()
host = socket.gethostname()
'''
Creating a object
'''
port = 6380 #Connecting to Port
s.connect((host , port))
'''
Host of your ip adress or Your machine hostname
'''
z = "Hi Server"
s.sendall(z.encode())#Sending Message
print("---Dred Client---")
print(s.recv(1024))
print("Time of Connection - ",datetime.datetime.now())
'''
Sending Messages in bytes with encoding 
'''
while True: #To Send Messages to Server
    r = input("\nType Messages to Send ")
    s.sendall(r.encode())
s.close()