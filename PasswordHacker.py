import socket, sys

# stocke les arguments de ligne de commande dans args
args = sys.argv

# creation d'un socket
client_socket = socket.socket()

# connexion a un serveur
hostname = args[1]  # car 0 c'est le nom du scripte
port = int(args[2])
address = (hostname, port)
client_socket.connect(address)

# envoi de donnees au serveur
data = args[3]
data = data.encode()
client_socket.send(data)

# reception de la reponse du serveur
response = client_socket.recv(1024)
response = response.decode()
print(response)
client_socket.close()