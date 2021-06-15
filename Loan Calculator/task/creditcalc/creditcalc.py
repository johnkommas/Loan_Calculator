import math
import argparse




def count_of_months(principal, payment, interest):
    i = (interest / 100) / (12 * 100 / 100)
    n = math.log(payment / (payment - i * principal), 1 + i)
    n = math.ceil(n)
    if n % 12 == 0:
        years = n / 12
        print(f'It will take {int(years)} years to repay this loan!')
    else:
        years = n // 12
        months = n % 12
        print(f'It will take {int(years)} years and {int(months)} months to repay this loan!')
    print(f'Overpayment = {int(payment * n - principal)}')


def credit_principal(payment, periods, interest):
    i = (interest / 12) / 100
    p = int(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    print(f'Your loan principal = {p}!')
    print(f'Overpayment {payment * periods - p}')


def annuity_monthly_payment(principal, periods, interest):
    i = (interest / 12) / 100
    a = (principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    if a != int(a):
        a = int(a) + 1
    else:
        a = int(a)
    print (f'Your annuity payment = {a}!')
    print(f'Overpayment = {a * periods - principal}')


def differentiate_payment(principal,periods, interest):
    i = (interest / 12) / 100
    P = principal
    n = periods
    sum = 0
    for x, m in enumerate(range(1,n+1)):
        result = P/n + i * (P - (P * (m-1))/n)
        result = math.ceil(result)
        sum += result
        print(f"Month {x+1}: payment is {result}")
    print(f'Overpayment = {sum - P}')


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Incorrect parameters")
    return ivalue


# Step 1
parser = argparse.ArgumentParser(description = "That's my Description")

# Step 2 add arguments
parser.add_argument('--type', choices=['annuity', 'diff'], help='Incorrect parameters')
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type = float)
parser.add_argument('--periods', type=check_positive )
parser.add_argument('--interest', type = float)

# Step 3 Reading from CMD
args = parser.parse_args()

if args.type == 'annuity' and args.principal and args.payment and args.interest:
    count_of_months(args.principal, args.payment, args.interest)
elif args.type == 'annuity' and args.principal  and args.periods and args.interest:
    annuity_monthly_payment(args.principal, args.periods, args.interest)
elif args.type == 'diff' and args.principal  and args.periods  and args.interest:
    differentiate_payment(args.principal, args.periods, args.interest)
elif args.type == 'annuity' and args.periods and args.payment  and args.interest:
    credit_principal(args.payment, args.periods, args.interest)
else:
    print('Incorrect parameters.')