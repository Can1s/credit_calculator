import math


print("Enter the credit principal:")
principal = int(input())
print("""What do you want to calculate? 
type "m" - for the count of months, 
type "p" - for the monthly payment:
""")
type_calculate = input()
if type_calculate.__eq__("p"):
    print("Enter the count of months:")
    count_of_months = int(input())
    monthly_payment = principal / count_of_months
    last_payment = principal - (count_of_months - 1) * math.ceil(monthly_payment)
    if monthly_payment == last_payment:
        print(f"Your monthly payment = {monthly_payment}")
    else:
        print(f"Your monthly payment = {math.ceil(monthly_payment)} with last month payment = {last_payment}")
elif type_calculate.__eq__("m"):
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    months = math.ceil(principal / monthly_payment)
    if months == 1:
        print(f"""
            It takes {months} month to repay the credit""")
    else:
        print(f"""
            It takes {months} months to repay the credit""")
