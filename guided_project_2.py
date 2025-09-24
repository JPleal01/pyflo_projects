# First task

print('''--------------------------------
----- FINANCIAL VISUALIZER -----
--------------------------------''')
salary = input("Annual Salary:\n")
housing = input("Monthly Housing:\n")
bills = input("Monthly Bills:\n")
food = input("Weekly Food:\n")
travel = input("Annual Travel:\n")

# Second task

def isntvalid (x):
    for i in x:
        if i.isnumeric() == False and i != '.' :
            return True
        else:
            return False
        
if isntvalid(salary) or isntvalid(housing) or isntvalid(bills) or isntvalid(food) or isntvalid(travel):
    print('Invalid input, please try again.')
else:
    print('All inputs confirmed valid.')
    
salarys = float(salary)
housings = float(housing)
billss = float(bills)
foods = float (food)
travels = float(travel)
    

# Third task

def taxvalue (x):
    salary = x
    if salary<= 10000:
        return salary*0.05
    if salary> 10000 and salary <= 40000:
        return salary*0.1
    if salary> 40000 and salary<= 80000:
        return salary*0.15
    if salary> 80000:
        return salary*0.2
        
tax = taxvalue(salary)
print(round(tax,2))

# Fourth task

def annual_percent (x, y):
    annual_spend = x
    salary = y
    tp = (annual_spend/salary)*100
    return tp
    
annual_bills = bills*12
annual_housing = housing * 12
annual_food = food*52


housing_percent = annual_percent(annual_housing, salary)
bills_percent=annual_percent(annual_bills,salary)
food_percent=annual_percent(annual_food,salary)
travel_percent=annual_percent(travel ,salary)
tax_percent = annual_percent(tax, salary)

extra =salary-(annual_housing +annual_bills+annual_food+travel+tax)

print(housing_percent)
print(bills_percent)
print(food_percent)
print(travel_percent)
print(tax_percent)
print(extra_percent)

# Fifth task

annual_salary  = 100000
annual_housing = 24000
annual_bills   = 8400
annual_food    = 5200
annual_travel  = 5000
annual_tax     = 20000
annual_extra   = 37400

percentage_housing = 24.0
percentage_bills   = 8.4
percentage_food    = 5.2
percentage_travel  = 5.0
percentage_tax     = 20.0
percentage_extra   = 37.4

width = int(max(percentage_tax, percentage_housing, percentage_bills, percentage_food, percentage_travel, percentage_extra))
boundary = '----------------------------------' + ('-' * width)
print()
print(boundary)
print('housing | $' + format(annual_housing, '11,.2f') + ' ', end='')
print('| ' + format(percentage_housing, '5,.1f') + '% | ' + ('#' * int(percentage_housing)))
print('  bills | $' + format(annual_bills, '11,.2f') + ' ', end='')
print('| ' + format(percentage_bills, '5,.1f') + '% | ' + ('#' * int(percentage_bills)))
print('   food | $' + format(annual_food, '11,.2f') + ' ', end='')
print('| ' + format(percentage_food, '5,.1f') + '% | ' + ('#' * int(percentage_food)))
print(' travel | $' + format(annual_travel, '11,.2f') + ' ', end='')
print('| ' + format(percentage_travel, '5,.1f') + '% | ' + ('#' * int(percentage_travel)))
print('    tax | $' + format(annual_tax, '11,.2f') + ' ', end='')
print('| ' + format(percentage_tax, '5,.1f') + '% | ' + ('#' * int(percentage_tax)))
print('  extra | $' + format(annual_extra, '11,.2f') + ' ', end='')
print('| ' + format(percentage_extra, '5,.1f') + '% | ' + ('#' * int(percentage_extra)))
print(boundary)


