print("Enter the age:")
age = int(input())

new_income = 0.00
if age>=18 and age<=60:
    print("Enter the income:")
    income = float(input())
    if income >= 0 and income <= 250000:
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income > 250000 and income <=500000:
        new_income = (income) * 0.1
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income > 500000 and income <=1000000:
        new_income = (income) * 0.2
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income >1000000:
        new_income = (income) * 0.3
        print("The Tax amount is: ",format(new_income,'.2f'))
    else:
        print("Invalid Income")
elif age>60 and age<=80:
    print("Enter the income:")
    income = float(input())
    if income >= 0 and income <= 300000:
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income > 300000 and income <=500000:
        new_income = (income) * 0.1
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income > 500000 and income <=1000000:
        new_income = (income) * 0.2
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income >1000000:
        new_income = (income) * 0.3
        print("The Tax amount is: ",format(new_income,'.2f'))
    else:
        print("Invalid Income")
elif age>80 and age<=100:
    print("Enter the income:")
    income = float(input())
    if income >= 0 and income <= 500000:
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income > 500000 and income <=1000000:
        new_income = (income) * 0.2
        print("The Tax amount is: ",format(new_income,'.2f'))
    elif income >1000000:
        new_income = (income) * 0.3
        print("The Tax amount is: ",format(new_income,'.2f'))
    else:
        print("Invalid Income")
else:
    print("Invalid Age")