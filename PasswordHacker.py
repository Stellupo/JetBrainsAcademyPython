import socket
import sys
import itertools

# cette fonction reformate les elements d'une liste en supprimant le saut de ligne et renvoie la nouvelle valeur
def reformat(file):
    for line in file:
        line = line.strip("\n")
        password = str(line)
        yield password

# cette fonction isole chaque lettre dans une sous-liste à laquelle
# on ajoute le même lettre mais en majuscule [['g','G'],['o','O']]
def combinaison(word):
    combo = []
    for letter in word:
        combo.append([letter.lower(), letter.upper()])
    return combo

# cette fonction cree des mdp à partir des lettres de la liste, alternant entre minuscule et majuscule
def password_creation(liste):
    for a in itertools.product(*liste):
        word = str("".join(a))
        yield word

# cette fonction envoie une data au serveur et retourne la réponse du serveur decryptée
def send_response(data):
    # envoi du mdp au serveur
    client_socket.send(data)
    # reception de la réponse du serveur
    response = client_socket.recv(1024)
    msg = response.decode()
    return msg

# cette fonction teste les differents mdp possibles tant que la reponse du serveur n'est pas positif
def main(msg,gen):
    while msg != "Connection success !":
        # recherche d'un mdp dans le fichier texte
        password = next(gen)
        # on teste les differentes ortograhpes du mot
        combo = combinaison(password)
        for i in password_creation(combo):
            data = i.encode()
            msg = send_response(data)
            if msg != "Connection success!":
                continue
            elif msg == "Connection success!":
                print(data.decode())
                return

# creation d'un socket
client_socket = socket.socket()

# stocke les arguments de ligne de commande dans args
args = sys.argv

# connexion a un serveur
hostname = args[1]  # car 0 c'est le nom du scripte
port = int(args[2])
address = (hostname, port)
client_socket.connect(address)

# ouverture du fichier texte
my_file = open(
    '/Users/estelle/Desktop/Développement Web/Password Hacker2/Password Hacker/Smarter, dictionary-based brute force/passwords.txt',
    "r")
# transformation du fichier en une liste
file_list = my_file.readlines()
# on reformate les mdp de la liste en str
gen = reformat(file_list)
# variable envoyee a la fonction principale
msg = ""
# appel de la fonction principale
main(msg,gen)
# fermeture du fichier texte
my_file.close()
# fermeture du serveur
client_socket.close()