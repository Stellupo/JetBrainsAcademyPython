import math
import argparse


def n_calculation ():
    interest = float(args.interest)/(12*100) #float pas %  i
    base = 1 + interest
    x = (args.payment / (args.payment - (interest * args.principal)))
    periods = math.ceil(math.log(x, base))
    if periods < 12:
        print("You need "+str(periods)+" months to repay this credit!")
    elif periods == 12:
        print("You need 1 year to repay this credit!")
    else:  #plus d'un an
        number_year = periods // 12
        number_month = periods % 12
        if number_month ==0:
            print("You need " + str(number_year) + " years to repay this credit!")
        else:
            print("You need "+str(number_year)+" years and "+str(number_month)+" months to repay this credit!")
        sum = args.payment*periods
        print('Overpayment = ' + str(math.ceil(sum - args.principal)))

def a_calculation():
    interest = float(args.interest)/(12*100) #float pas %  i
    annuity_payment = args.principal*((interest*(1+interest)**args.periods)/((1+interest)**args.periods-1))
    annuity_payment = math.ceil(annuity_payment)
    print ("Your annuity payment = "+str(annuity_payment)+"!")
    sum = annuity_payment * args.periods
    print('Overpayment = ' + str(math.ceil(sum - args.principal)))

def p_calculation():
    interest = float(args.interest) / (12 * 100)  # float pas %  i
    credit_principal = args.payment/((interest*(1+interest)**args.periods)/((1+interest)**args.periods-1))
    credit_principal = math.floor(credit_principal)
    print("Your credit principal = "+str(credit_principal)+"!")
    sum = args.payment * args.periods
    print('Overpayment = ' + str(math.ceil(sum - credit_principal)))

def diff_type() :
    if args.payment == None and args.principal > 0 and args.periods > 0 and args.interest > 0:
        interest = float(args.interest) / (12 * 100)  # float pas %  i
        count = 1
        sum = 0
        while args.periods >= count:
            diff = (args.principal / args.periods) + interest * (
                    args.principal - ((args.principal * (count - 1)) / args.periods))
            diff = math.ceil(diff)
            print('Month ' + str(count) + ' :paid out ' + str(diff))
            count += 1
            sum += diff
        print('Overpayment = ' + str(math.ceil(sum - args.principal)))
    else:
        print('Incorrect parameters')

def annuity_type():
    if args.periods == None and args.principal > 0 and args.payment > 0 and args.interest > 0:
        n_calculation()
    elif args.payment == None and args.principal > 0 and args.periods > 0 and args.interest > 0:
        a_calculation()
    elif args.principal == None and args.periods > 0 and args.payment > 0 and args.interest > 0:
        p_calculation()
    else:
        print("Incorrect parameters")

if __name__ == '__main__':
    #Initialisation de l'analyser
    parser = argparse.ArgumentParser()
    # Paramètres optionnels :
    parser.add_argument('--type', help='What type of credit do you have ?type "diff" for a differentiated payment, '
                                            'type "annuity" for a annuity payment')
    parser.add_argument('--principal', help='Enter credit principal',type = int)
    parser.add_argument('--payment', help='Enter payment ',type = int)
    parser.add_argument('--periods', help='Enter periods ', type=int)
    parser.add_argument('--interest', help='Enter interest', type=float)
    # Analyse les arguments :
    args = parser.parse_args()
    list_args = [args.type, args.principal, args.payment, args.periods, args.interest]
    list_args_sorted = []
    for arguments in list_args:
        if arguments == None:
            continue
        else:
            list_args_sorted += [arguments]
    if len(list_args_sorted) < 4:
        print("Incorrect parameters")
    elif len(list_args_sorted) >= 4: # Au moins 4 arguments
        if args.type == "diff" or args.type == "annuity":
            if args.type == "diff":
                if args.payment != None:
                    print("Incorrect parameters")
                else:
                    diff_type()
            elif args.type == "annuity":
                annuity_type()
        else:
            print("Incorrect parameters")