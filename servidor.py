import socket
import pickle

servidorsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

servidorsocket.bind((host, port))

servidorsocket.listen()
print("Server running...\n")
while True:
    servidorsocket.listen()
    clientesocket, addr = servidorsocket.accept()
    print("Conectado a %s" % str(addr))
    data = clientesocket.recv(1024)
    data = pickle.loads(data)
    resp = data[0]
    val1 = data[1]
    print(data)
    if resp == 1:
        val1 = (val1*100)

    if resp == 2:
        val1 = (val1/1000)

    if resp == 3:
        val1 = (val1*100**2)

    if resp == 4:
        val1 = (val1/1000**2)

    if resp == 5:
        val1 = (val1*100**3)

    if resp == 6:
        val1 = (val1/1000**3)
    val1 = pickle.dumps(val1)
    clientesocket.send(val1)
    clientesocket.close()
