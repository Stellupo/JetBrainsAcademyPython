import sqlite3
import random

# Creation database
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT , balance INTEGER DEFAULT 0)')
conn.commit()
cur.execute('DROP TABLE card')  # reinitialisation de la table, pour vider la mémoire
conn.commit()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT , balance INTEGER DEFAULT 0)')
conn.commit()

class BankMachine:
    def __init__(self):
        self.state_bank = "Home"
        self.clients_database = []
        self.start_menu()
        self.balance = 0
        self.card_number = []
        self.code_pin = []

    def start_menu(self):
        print('''
1. Create an account
2. Log into account
0. Exit''')
        self.state_bank = "Home"

    def account_menu(self):
        print('''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
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
            self.card_number = [4, 0, 0, 0, 0, 0]
            self.code_pin = []
            for i in range(10):  # on ajoute 9 chiffres pour avoir 15 chiffres dans le num carte
                numbers = random.randint(0, 9)
                self.card_number.append(numbers)
            count = 0
            luhn_test = []
            for x in self.card_number[:15]:
                if count % 2 == 0:
                    luhn_test.append(2 * x)
                elif count % 2 == 1:
                    luhn_test.append(x)
                count += 1
            luhn_test = [y - 9 if y > 9 else y for y in luhn_test]
            card_number_test = self.card_number[:15]
            card_number_test.extend([w for w in range(0, 9) if (sum(luhn_test) + w) % 10 == 0])
            if self.card_number == card_number_test:
                self.card_number = ''.join(str(numbers) for numbers in self.card_number)
                if self.card_number not in self.clients_database:  # vérifier que le num soit unique
                    self.clients_database.append(self.card_number)
                    for i in range(4):
                        x = random.randint(0, 9)
                        self.code_pin.append(x)
                    self.code_pin = ''.join(str(numbers) for numbers in self.code_pin)
                    self.clients_database.append(self.code_pin)
                    print('\n' + 'Your card has been created')
                    print('Your card number:', self.card_number, sep="\n")
                    print('Your card PIN:', self.code_pin, sep="\n")
                    self.database()
                    break
                elif self.card_number in self.clients_database:
                    continue
            elif self.card_number != card_number_test:
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
        if user_choice == 1:
            print("\n" + "Balance: ", self.balance)
            self.account_menu()
        elif user_choice == 2:  # todo il va falloir ajouter la balance au registre de la database j'imagine
            print('Enter income:')
            deposit_money = int(input())
            self.balance += deposit_money
            print('Income was added!')
            self.account_menu()
        elif user_choice == 3:
            print('Transfer', 'Enter card number:', sep='\n')
            card_number = input()
            if card_number in self.clients_database and card_number == self.card_number:
                print("You can't transfer money to the same account!")
            elif card_number in self.clients_database and card_number != self.card_number:
                print('Enter how much money you want to transfer:')
                transfer_money = int(input())
                self.balance +=  #todo update !
        elif user_choice == 4:
            cur.execute('DELETE FROM card WHERE number = ?', (self.card_number, ))
            print('The account has been closed!')
            self.start_menu()
        elif user_choice == 5:
            print("\n" + "You have successfully logged out!")
            self.start_menu()
        else:
            self.state_bank = "Account"
            print('Invalid answer')

    def database(self):
        req = 'INSERT INTO card (number, pin) VALUES (?,?)'
        cur.execute(req, (self.card_number, self.code_pin))  #
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

#todo cleaner la liste client_database et la remplacer par la base de données directement.