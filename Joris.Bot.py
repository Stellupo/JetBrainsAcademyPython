def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

def test():
    print("Let's test your programming knowledge.")
    while True :
        print('''
        What am I ?
        1. A simple program you have created
        2. An alien for another dimension
        3. A superHero named Vision
        4. An AI you should be scared of ''')
        user_answer = input ()
        if user_answer in ["2","3","4"]:
            print ("Please, try again!")
            continue
        else:
            print("You're really smart!")
            break

def end():
    print('Congratulations, I wish you have a nice day!')


greet('Joris', 'a long time ago, by Mr.Strak')  # change it as you need
remind_name()
guess_age()
count()
test()
end()