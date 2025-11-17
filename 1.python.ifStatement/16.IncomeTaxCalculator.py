total_income=int(input("Give the Total income of this Year="))
Exemptions_and_Deductions=int(input("how  much you spent on the house rent and health insurance="))
total_amount_to_pay_tax = (total_income)-(Exemptions_and_Deductions)
if total_amount_to_pay_tax<=250000:
    print(f"Your income is {total_amount_to_pay_tax} that was less than 2,50,000 you do not need to pay tax")
else:
    if total_amount_to_pay_tax<=500000:
    total=(total_amount_to_pay_tax-250000)*(5/100)
    elif total_amount_to_pay_tax<=1000000:
    total=(250000)*(5/100)+(total_amount_to_pay_tax-500000)*(20/100)
    else :
    total=(250000)*(5/100)+(500000)*(20/100)+(total_amount_to_pay_tax-1000000)*(30/100)
    print(f"Your total income is {total_amount_to_pay_tax}. your tax amount is {total}")