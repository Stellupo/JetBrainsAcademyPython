import math

def n_calculation ():
    print("Enter credit principal")
    credit_principal = float(input())  #P
    print("Enter monthly payment:")
    annuity_payment = float(input())  #A
    print("Enter credit interest")
    interest = float(input())/(12*100) #float pas %  i
    base = 1 + interest
    x = (annuity_payment / (annuity_payment - (interest * credit_principal)))
    number_payment = math.ceil(math.log(x, base))
    print (number_payment)
    if number_payment < 12:
        print("You need "+str(number_payment)+" months to repay this credit!")
    elif number_payment == 12:
        print("You need 1 year to repay this credit!")
    else:  #plus d'un an
        number_year = number_payment // 12
        number_month = number_payment % 12
        print("You need "+str(number_year)+" years and "+str(number_month)+" months to repay this credit!")

def a_calculation():
    print("Enter credit principal")
    credit_principal = float(input())  #P
    print("Enter count of periods")
    number_payment = float(input())  #n
    print("Enter credit interest")
    interest = float(input())/(12*100) #float pas %  i
    print("Enter count of months:")
    annuity_payment = credit_principal*((interest*(1+interest)**number_payment)/((1+interest)**number_payment-1))
    annuity_payment = math.ceil(annuity_payment)
    print ("Your annuity payment = "+str(annuity_payment)+"!")

def p_calculation():
    print("Enter monthly payment:")
    annuity_payment = float(input())  #A
    print("Enter count of periods")
    number_payment = float(input())  # n
    print("Enter credit interest")
    interest = float(input()) / (12 * 100)  # float pas %  i
    credit_principal = annuity_payment/((interest*(1+interest)**number_payment)/((1+interest)**number_payment-1))
    credit_principal = math.ceil(credit_principal)
    print("Your credit principal = "+str(credit_principal)+"!")


print('''
What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal:
''')
calcul_needed = input()
if calcul_needed == "n":
    n_calculation()
elif calcul_needed == "a":
    a_calculation()
elif calcul_needed == "p":
    p_calculation()




#Etape 2 :
    '''
    monthly_counts = int(input())
    monthly_payment = math.ceil(credit_principal/monthly_counts)

    print(monthly_payment)
    final_month = credit_principal-(monthly_counts-1) * monthly_payment
    if monthly_payment != final_month :
        print('Your monthly payment = '+ str(monthly_payment) + " with last month payment = " + str(final_month) +".")
    else:
        print('Your monthly payment = '+ str(monthly_payment))
elif calcul_needed == "a":
    print("Enter count of months:")
else:
    print("Uncorrect answer, try again")'''