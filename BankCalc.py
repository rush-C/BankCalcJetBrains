import sys
import argparse
from math import log
from math import ceil

# Argparse input and input formatting

parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--type")
args = parser.parse_args()

# Input validation and calculations
if len(sys.argv) < 5:
    print("Incorrect parameters.")
else:
    # Differentiated payment calculations
    if args.type == 'diff':
        if args.payment != None:
            print("Incorrect parameters")
        else:
            i = args.interest / 1200
            if args.principal < 0 or args.periods < 0 or args.interest < 0:
                print("Incorrect parameters")
            else:
                total = 0
                for x in range(args.periods):
                    diffPay = args.principal / (args.periods) + i * (args.principal - args.principal * x / args.periods)
                    diffPay = ceil(diffPay)
                    print("Month {}: paid out {}".format(x+1, diffPay))
                    total = total + diffPay
                print()
                print("Overpayment = {}".format(total - args.principal))

    # Annuity payment calculations
    elif args.type == 'annuity':
        if args.interest == None:
            print("Incorrect parameters")
        else:
            i = args.interest / 1200
            if args.principal == None :
                if args.payment < 0 or args.periods < 0 or args.interest < 0:
                    print("Incorrect parameters")
                else:
                    new_principal = int(args.payment / ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)))
                    print("Your credit principal = {}!".format(new_principal))
                    print("Overpayment = {}".format(args.payment * args.periods - new_principal))
            elif args.payment == None:
                if args.principal < 0 or args.periods < 0 or args.interest < 0:
                    print("Incorrect parameters")
                else:
                    pay = args.principal * i * (1 + i) ** args.periods / ((1 + i) ** args.periods - 1)
                    pay = ceil(pay)
                    print("Your annuity payment = {}!".format(pay))
                    print("Overpayment = {}".format(pay * args.periods - args.principal))
            elif args.periods == None:
                if args.principal < 0 or args.payment < 0 or args.interest < 0:
                    print("Incorrect parameters")
                else:
                    period = log(args.payment / (args.payment - i * args.principal), (1 + i))
                    period = ceil(period)
                    years = period // 12
                    months = period % 12
                    if months == 0:
                        print("You need {} years to repay this credit!".format(years))
                    else:
                        if years == 0:
                            print("You need {} months to repay this credit!".format(months))
                        else:
                            print("You need {} years and {} months to repay this credit!".format(years, months))
                    print("Overpayment = {}".format(period * args.payment - args.principal))

    else:
        print("Incorrect parameters")


