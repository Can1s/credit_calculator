import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--payment', type=float)
parser.add_argument('--interest', type=float)
args = parser.parse_args()
type_ = args.type
principal = args.principal
periods = args.periods
payment = args.payment
interest = args.interest
if (type_ is not None) and (payment is not None) and (periods is not None) and (interest is not None):
    i = interest / (12 * 100)
    p = math.ceil(payment / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
    print(f"Your credit principal = {p}!")
elif (type_ is not None) and (principal is not None) and (periods is not None) and (interest is not None):
    i = interest / (12 * 100)
    if type_.__eq__("annuity"):
        a = math.ceil(principal * (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
        print(f"Your annuity payment = {a}!")
    else:
        overpayment = 0
        m = 1
        for k in range(periods):
            D = math.ceil(principal / periods + i * (principal - (principal * (m - 1) / periods)))
            overpayment += D
            print(f"Month {m}: paid out {D}")
            m += 1
        print(f"Overpayment = {overpayment - principal}")
elif (type_ is not None) and (principal is not None) and (payment is not None) and (interest is not None):
    i = interest / (12 * 100)
    n = math.ceil(math.log((payment / (payment - i * principal)), i + 1))
    overpayment = int(payment * n - principal)
    years = n // 12
    months = n - years * 12
    if months == 0:
        print(f"You need {years} years to repay this credit!")
        print(f"Overpayment = {overpayment}")
    elif years == 0:
        print(f"You need {months} months to repay this credit!")
        print(f"Overpayment = {overpayment}")
    else:
        print(f"You need {years} years and {months} months to repay this credit!")
        print(f"Overpayment = {overpayment}")
else:
    print("Incorrect parameters.")
