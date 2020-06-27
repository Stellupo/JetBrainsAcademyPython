class CoffeeMachine:

    def __init__(self, water_machine, milk_machine, coffee_machine, disposable_cups, money):
        self.water_machine = water_machine
        self.milk_machine = milk_machine
        self.coffee_machine = coffee_machine
        self.disposable_cups = disposable_cups
        self.money = money
        self.state_machine = "Home"
        self.step = 0
        self.change_home()

    def expresso(self):
        expresso_ingredients = [250, 0, 16]
        expresso_cost = 4
        if self.water_machine > expresso_ingredients[0] and self.milk_machine > expresso_ingredients[
            1] and self.coffee_machine > expresso_ingredients[2] and self.disposable_cups > 0:
            self.water_machine = self.water_machine - expresso_ingredients[0]
            self.milk_machine = self.milk_machine - expresso_ingredients[1]
            self.coffee_machine = self.coffee_machine - expresso_ingredients[2]
            self.disposable_cups -= 1
            self.money = self.money + expresso_cost
            print('I have enough resources, making you a coffee!')
        elif self.water_machine < expresso_ingredients[0]:
            print('Sorry, not enough water')
        elif self.milk_machine < expresso_ingredients[1]:
            print('Sorry, not enough milk')
        elif self.coffee_machine < expresso_ingredients[2]:
            print('Sorry, not enough coffee beans')
        elif self.disposable_cups < 1:
            print('Sorry, not enough cups')

    def latte(self):
        latte_ingredients = [350, 75, 20]
        latte_cost = 7
        if self.water_machine > latte_ingredients[0] and self.milk_machine > latte_ingredients[
            1] and self.coffee_machine > \
                latte_ingredients[2] and self.disposable_cups > 0:
            self.water_machine = self.water_machine - latte_ingredients[0]
            self.milk_machine = self.milk_machine - latte_ingredients[1]
            self.coffee_machine = self.coffee_machine - latte_ingredients[2]
            self.disposable_cups -= 1
            self.money = self.money + latte_cost
            print('I have enough resources, making you a coffee!')
        elif self.water_machine < latte_ingredients[0]:
            print('Sorry, not enough water')
        elif self.milk_machine < latte_ingredients[1]:
            print('Sorry, not enough milk')
        elif self.coffee_machine < latte_ingredients[2]:
            print("Sorry, I don't have enough stocks, I can't make you a coffee")
        elif self.disposable_cups < 1:
            print('Sorry, not enough cups')

    def cappuccino(self):
        cappuccino_ingredients = [200, 100, 12]
        cappuccino_cost = 6
        if self.water_machine > cappuccino_ingredients[0] and self.milk_machine > cappuccino_ingredients[
            1] and self.coffee_machine > \
                cappuccino_ingredients[2] and self.disposable_cups > 0:
            self.water_machine = self.water_machine - cappuccino_ingredients[0]
            self.milk_machine = self.milk_machine - cappuccino_ingredients[1]
            self.coffee_machine = self.coffee_machine - cappuccino_ingredients[2]
            self.disposable_cups -= 1
            self.money = self.money + cappuccino_cost
            print('I have enough resources, making you a coffee!')
        elif self.water_machine < cappuccino_ingredients[0]:
            print('Sorry, not enough water')
        elif self.milk_machine < cappuccino_ingredients[1]:
            print('Sorry, not enough milk')
        elif self.coffee_machine < cappuccino_ingredients[2]:
            print("Sorry, I don't have enough stocks, I can't make you a coffee")
        elif self.disposable_cups < 1:
            print('Sorry, not enough cups')

    def fill_action(self,action_user):
        if self.step == 0:
            self.water_machine = self.water_machine + int(action_user)
            self.step = 1
            print('Write how many ml of milk do you want to add:')
        elif self.step == 1:
            self.milk_machine = self.milk_machine + int(action_user)
            self.step = 2
            print('Write how many grams of coffee beans do you want to add:')
        elif self.step == 2:
            self.coffee_machine = self.coffee_machine + int(action_user)
            self.step = 3
            print('Write how many disposable cups of coffee do you want to add:')
        elif self.step ==3:
            self.disposable_cups = self.disposable_cups + int(action_user)
            self.step =0
            self.change_home()


    def remaining_action(self):
        print('The coffee machine has:')
        print(str(self.water_machine) + ' of water')
        print(str(self.milk_machine) + ' of milk')
        print(str(self.coffee_machine) + ' of coffee beans')
        print(str(self.disposable_cups) + ' of disposable cups')
        print(str(self.money) + ' of money')

    def take_action(self):
        print("I gave you", self.money, "$")
        self.money = 0

    def buy_action(self):
        print('''
            What do you want to buy ?
            1 - expresso
            2 - latte
            3 - cappuccino
            4 - back to main menu
            ''')
        self.state_machine = "choosing_coffee_state"

    def get_action_user(self, action_user):
        if self.state_machine == "Home":
            if action_user == "buy":
                self.buy_action()
            elif action_user == "fill":
                self.state_machine = "fill_state"
                print('Write how many ml of water do you want to add:')
            elif action_user == "take":
                coffee_instance.take_action()
                self.change_home()
            elif action_user == "remaining":
                coffee_instance.remaining_action()
                self.change_home()
            else:
                print("Your answer is incorrect, please try again")
                self.change_home()
        elif self.state_machine == "choosing_coffee_state":
            if action_user != "4" or action_user != "back":
                action_user = int(action_user)
                if action_user == 1 or action_user == 2 or action_user == 3:
                    if action_user == 1:
                        self.expresso()
                    elif action_user == 2:
                        self.latte()
                    elif action_user == 3:
                        self.cappuccino()
                else:
                    print("Your answer is incorrect, please try again")
            else:
                print("Come back to main menu ! ")
            self.change_home()
        elif self.state_machine == "fill_state":
            self.fill_action(action_user)




    def change_home(self):
        print('Write action (buy, fill, take, remaining, exit)')
        self.state_machine = "Home"


# if__name__=='__main__':
coffee_instance = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    action_user = input()
    if action_user == "exit":
        print("Have a nice day, bye!")
        break
    coffee_instance.get_action_user(action_user)

# Attention ! si une classe a besoin d'une var pr fonctionner, il faut qu'elle lui appartienne (ou à son instance).
# Donc self.state_machine doit être ds la classe ! (cf.Humain et barre de satiété)
# si on ne veut pas créer de valeur globale, il suffit de créer une fonction et de l'appeler.
#shadows name : en gros, ma variable va être remplacée dans la fonction/méthode