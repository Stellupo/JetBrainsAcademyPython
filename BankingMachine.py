import sqlite3
import random

# Creation database
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT , balance INTEGER DEFAULT 0)')
conn.commit()
# reinitialisation de la table, pour vider la mémoire lors des tests
'''cur.execute('DROP TABLE card')
conn.commit()
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT , balance INTEGER DEFAULT 0)')
conn.commit()'''

class BankMachine:
    def __init__(self):
        self.state_bank = "Home"
        self.start_menu()
        self.card_number = []
        self.code_pin = []

    def start_menu(self): # menu Home
        print('''
1. Create an account
2. Log into account
0. Exit''')
        self.state_bank = "Home"

    def account_menu(self): # menu Account (une fois loggin a un compte)
        print('''
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
''')
        self.state_bank = "Account"

    def action_user(self, user_choice): # input du user determine les prochaines actions
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

    def luhn_test(self,var_card): # on vérifie que le num de carte reussisse le test de luhn
        count = 0
        luhn_test = []
        for num in range(len(var_card)): # au cas ou la carte est un input string, conversion en chiffres
            var_card[num] = int(var_card[num])
        for x in var_card[:15]:
            if count % 2 == 0:
                luhn_test.append(2 * int(x))
            elif count % 2 == 1:
                luhn_test.append(int(x))
            count += 1
        luhn_test = [y - 9 if y > 9 else y for y in luhn_test]
        card_number_test = var_card[:15]
        card_number_test.extend([w for w in range(0, 9) if (sum(luhn_test) + w) % 10 == 0])
        if var_card == card_number_test:  # si le test est un succes
            return True
        else:
            return False

    def create_account(self):
        while True:
            self.card_number = [4, 0, 0, 0, 0, 0]
            self.code_pin = []
            for i in range(10):  # on ajoute 9 chiffres pour avoir 15 chiffres dans le num carte
                numbers = random.randint(0, 9)
                self.card_number.append(numbers)
            if self.luhn_test(self.card_number):
                self.card_number = ''.join(str(numbers) for numbers in self.card_number)
                table = self.database_card()
                if (self.card_number,) not in table:  # on vérifie que le num soit unique
                    for i in range(4):
                        x = random.randint(0, 9)
                        self.code_pin.append(x)
                    self.code_pin = ''.join(str(numbers) for numbers in self.code_pin)
                    print('\n' + 'Your card has been created')
                    print('Your card number:', self.card_number, sep="\n")
                    print('Your card PIN:', self.code_pin, sep="\n")
                    self.database_add()
                    break
                elif (self.card_number,) not in table:
                    continue
            elif not self.luhn_test(self.card_number):
                continue

    def login(self):
        print('\n' + 'Enter your card number: ')
        card_number = input()
        print('Enter your PIN: ')
        code_pin = input()
        table = self.database_card_pin()
        if (card_number,code_pin) not in table:
            print('\n' + "Wrong card number or PIN!")
            self.start_menu()
        elif (card_number,code_pin) in table:
                print('\n' + "You have successfully logged in!")
                self.card_number = card_number
                self.code_pin = code_pin
                self.account_menu()

    def user_account(self, user_choice):
        if user_choice == 1:
            balance = self.balance_value()
            print("\n" + "Balance: ", balance)
            self.account_menu()
        elif user_choice == 2:
            self.add_money()
            self.account_menu()
        elif user_choice == 3:
            self.transfer_money()
            self.account_menu()
        elif user_choice == 4:
            cur.execute('DELETE FROM card WHERE number = ?', (self.card_number, ))
            conn.commit()
            print('The account has been closed!')
            self.start_menu()
        elif user_choice == 5:
            print("\n" + "You have successfully logged out!")
            self.start_menu()
        else:
            print('Invalid answer')
            self.account_menu()

    def add_money(self):
        print('Enter income:')
        deposit_money = int(input())
        balance = self.balance_value()
        balance += deposit_money
        print('Income was added!')
        req = 'UPDATE card SET balance = ? WHERE number = ?'
        cur.execute(req, (balance, self.card_number))
        conn.commit()

    def transfer_money(self):
        print('Transfer', 'Enter card number:', sep='\n')
        card_number = input()
        table = self.database_card()
        balance = self.balance_value()
        if not self.luhn_test(list(card_number)):
            print('Probably you made mistake in the card number. Please try again!')
        elif (str(card_number),) not in table:
            print("Such a card does not exist.")
        elif (card_number,) in table and card_number == self.card_number:
            print("You can't transfer money to the same account!")
        elif (card_number,) in table and card_number != self.card_number:
            print('Enter how much money you want to transfer:')
            transfer_money = int(input())
            if transfer_money <= balance:
                balance -= transfer_money  # l'argent est enlevé du compte débiteur
                req = 'UPDATE card SET balance = ? WHERE number = ?'
                cur.execute(req, (balance, self.card_number))
                conn.commit()
                req = 'UPDATE card SET balance = balance +? WHERE number = ?'  # l'argent est rajouté sur le compte créditeur
                cur.execute(req, (transfer_money, card_number))
                conn.commit()
                print('Success!')
            elif transfer_money > balance:
                print("Not enough money!")

    def database_add(self):  # ajout des coordonnees bancaires et impression de la table
        req = 'INSERT INTO card (number, pin) VALUES (?,?)'
        cur.execute(req, (self.card_number, self.code_pin))  #
        conn.commit()
        cur.execute('SELECT * FROM card')
        table = cur.fetchall()
        print(table)

    def database_card_pin(self): # je vérifie que ma carte et mon code pin ne soient pas déjà dans ma base de données
        cur.execute('SELECT number, pin FROM card')
        table = cur.fetchall()
        return table

    def database_card(self):
        cur.execute('SELECT number FROM card')
        table = cur.fetchall()
        return table

    def balance_value(self):
        cur.execute('SELECT balance FROM card WHERE number = ?;', (self.card_number,))
        table_balance = cur.fetchone()
        balance = int(table_balance[0])
        return balance

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