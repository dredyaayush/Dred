import socket,time,datetime,hashlib
'''
Socket is most important module for network binding
'''
s = socket.socket()#Creating a object
print("-------------------Dred-----------------------")
userin = input("\n1.New User\n2.Existing User\n3.Check History\n4.Help\nChoose ")
if userin == "4": #For Help
    print("\nWhat if you choose New User Option?\nYou will redirected to a new fresh network between server and client.\nBut if you choose option 2 then you will be able to access to history of data\nIf you choose 1 then you will lost your history in you file.")
    print("\nThis works as a server connector to clients where client is strongly connected to server and transmiss data to server")
    exit()
if userin == "3": #For accesing history direct from command line.
    with open("LapyData.txt",mode="r") as read:
        ac = read.read()
        print("\nHistory--")
        read.close()
    exit()
port = 6380 #Creating a Port
s.bind(('', port))
'''
s.bind with any ip adrress and port of 6380
'''
print("\nBinded")
s.listen(5) #Waiting for 5 connections for connect
print("Connecting")
while True: #For New Messages and Connection
    c,addr = s.accept()
    print("\nGot Connection",addr,datetime.datetime.now())
    if userin == "2":
        History = ()
        with open("LapyData.txt",mode = "r") as f: #For Returning One..
            f.read()
            f.close()
        ap = "Server - Thanks For Connecting"
        c.send(ap.encode())
        recieve = str(c.recv(1024))
        print(recieve,"\n")
        while True:
            recieve2 = str(c.recv(1024))
            with open("LapyData.txt" ,mode="a") as file:
                file.write("\n"+recieve2+" "+str(datetime.datetime.now()))
                file.close()
            print(recieve2,datetime.datetime.now())
    if userin == "1":
        History = ()
        with open("LapyData.txt", mode="w") as f:  # For New One One..
            f.write(str(History))
            f.close()
        ap = "Server - Thanks For Connecting"
        c.send(ap.encode())
        recieve = str(c.recv(1024))
        print(recieve, "\n")
        while True:
            recieve2 = str(c.recv(1024))
            with open("LapyData.txt", mode="a") as file:
                file.write("\n" + recieve2+" "+str(datetime.datetime.now()))
                file.close()
            print(recieve2, datetime.datetime.now())
    c.close()