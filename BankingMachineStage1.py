import random


class BankMachine:
    def __init__(self):
        self.state_bank = "Home"
        user_choice = ""
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
        card_number = [4, 0, 0, 0, 0, 0]
        code_pin = []
        for i in range(10):
            numbers = random.randint(0, 9)
            card_number.append(numbers)
        card_number = ''.join(str(numbers) for numbers in card_number)
        for i in range(4):
            x = random.randint(0, 9)
            code_pin.append(x)
        code_pin = ''.join(str(numbers) for numbers in code_pin)
        if card_number not in self.clients_database:
            print('\n' + 'Your card has been created')
            print('Your card number:', card_number, sep="\n")
            print('Your card PIN:', code_pin, sep="\n")
            self.clients_database.append(card_number)
            self.clients_database.append(code_pin)
        else:
            self.create_account()

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