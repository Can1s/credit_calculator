import math


print("""What do you want to calculate? 
type "n" for the count of months, 
type "a" for the annuity monthly payment,
type "p" for credit principal:""")
type_calculate = input()
if type_calculate.__eq__("n"):
    print("Enter the credit principal:")
    credit_principal = int(input())
    print("Enter monthly payment:")
    annuity_payment = float(input())
    print("Enter credit interest:")
    credit_interest = float(input())
    i = credit_interest / (12 * 100)
    n = math.ceil(math.log((annuity_payment / (annuity_payment - i * credit_principal)), i+1))
    years = n // 12
    months = n - years * 12
    print(f"You need {years} years and {months} months to repay this credit!")
elif type_calculate.__eq__("a"):
    print("Enter the credit principal:")
    credit_principal = int(input())
    print("Enter count of periods:")
    count_of_periods = float(input())
    print("Enter credit interest:")
    credit_interest = float(input())
    i = credit_interest / (12 * 100)
    a = math.ceil(credit_principal * (i * math.pow(1+i, count_of_periods) / (math.pow(1+i, count_of_periods) - 1)))
    print(f"Your annuity payment = {a}!")
elif type_calculate.__eq__("p"):
    print("Enter monthly payment:")
    annuity_payment = float(input())
    print("Enter count of periods:")
    count_of_periods = float(input())
    print("Enter credit interest:")
    credit_interest = float(input())
    i = credit_interest / (12 * 100)
    p = math.ceil(annuity_payment / (i * math.pow(1 + i, count_of_periods) / (math.pow(1 + i, count_of_periods) - 1)))
    print(f"Your credit principal = {p}!")
