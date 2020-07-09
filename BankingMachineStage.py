import sqlite3
import random

# on ne doit le faire qu'une fois ! Pas chaque fois qu'une fonction est appelée

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT , balance INTEGER DEFAULT 0)')
conn.commit()
cur.execute('DROP TABLE card')  # réinitialisation de la table, pour vider la mémoire
conn.commit()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT , balance INTEGER DEFAULT 0)')
conn.commit()

class BankMachine:
    def __init__(self):
        self.state_bank = "Home"
        self.clients_database = []
        self.start_menu()

    def start_menu(self):
        print('''
1. Create an account
2. Log into account
0. Exit''')
        self.state_bank = "Home"

    def account_menu(self):
        print('''
1. Balance
2. Log out
0. Exit
''')
        self.state_bank = "Account"

    def action_user(self, user_choice):
        if self.state_bank == "Home":
            if user_choice == 1:
                self.create_account()
                self.start_menu()
            elif user_choice == 2:
                self.login()
            elif user_choice != 1 and user_choice != 2:
                print('Invalid answer')
        elif self.state_bank == "Account":
            self.user_account(user_choice)

    def create_account(self):
        while True:
            card_number = [4, 0, 0, 0, 0, 0]
            code_pin = []
            for i in range(10):  # on ajoute 9 chiffres pour avoir 15 chiffres dans le num carte
                numbers = random.randint(0, 9)
                card_number.append(numbers)
            count = 0
            luhn_test = []
            for x in card_number[:15]:
                if count % 2 == 0:
                    luhn_test.append(2 * x)
                elif count % 2 == 1:
                    luhn_test.append(x)
                count += 1
            luhn_test = [y - 9 if y > 9 else y for y in luhn_test]
            card_number_test = card_number[:15]
            card_number_test.extend([w for w in range(0, 9) if (sum(luhn_test) + w) % 10 == 0])
            if card_number == card_number_test:
                card_number = ''.join(str(numbers) for numbers in card_number)
                if card_number not in self.clients_database:  # vérifier que le num soit unique
                    self.clients_database.append(card_number)
                    for i in range(4):
                        x = random.randint(0, 9)
                        code_pin.append(x)
                    code_pin = ''.join(str(numbers) for numbers in code_pin)
                    self.clients_database.append(code_pin)
                    print('\n' + 'Your card has been created')
                    print('Your card number:', card_number, sep="\n")
                    print('Your card PIN:', code_pin, sep="\n")
                    self.database(card_number, code_pin)
                    break
                elif card_number in self.clients_database:
                    continue
            elif card_number != card_number_test:
                continue

    def login(self):
        print('\n' + 'Enter your card number: ')
        card_number = input()
        print('Enter your PIN: ')
        code_pin = input()
        if card_number not in self.clients_database or code_pin not in self.clients_database:
            print('\n' + "Wrong card number or PIN!")
            self.start_menu()
        else:
            if self.clients_database.index(card_number) == (self.clients_database.index(code_pin) - 1):
                print('\n' + "You have successfully logged in!")
                self.account_menu()
            else:
                print('\n' + "Wrong card number or PIN!")
                self.start_menu()

    def user_account(self, user_choice):
        balance = 0
        if user_choice == 1:
            print("\n" + "Balance: ", balance)
            self.account_menu()
        elif user_choice == 2:
            print("\n" + "You have successfully logged out!")
            self.start_menu()
        else:
            self.state_bank = "Account"
            print('Invalid answer')

    def database(self, card_number, code_pin):
        req = 'INSERT INTO card (number, pin) VALUES (?,?)'
        cur.execute(req, (card_number, code_pin))
        conn.commit()
        cur.execute('SELECT * FROM card')
        table = cur.fetchall()
        print(table)


# main
banking_instance = BankMachine()
while True:
    try:
        user_choice = int(input())
        if user_choice == 0:
            print('\n' + 'Bye!')
            break
        banking_instance.action_user(user_choice)
    except ValueError:
        print('Invalid answer')
        continue
