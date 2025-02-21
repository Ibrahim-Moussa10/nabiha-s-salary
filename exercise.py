
salary = float(input("Enter your salary: "))

if salary < 0:

    print("Salary must be a positive number.")
    quit()

month = input("Enter the month: ")

if month.lower() not in ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]:
    
    print("Invalid month.")
    quit()

savings_percentage = float(input("Enter the savings percentage: "))

if savings_percentage < 0 or savings_percentage > 100:

    print("Savings percentage must be between 0 and 100.")
    quit()

rent_percentage = float(input("Enter the rent percentage: "))

electricity_percentage = float(input("Enter the electricity percentage: ")) 

savings = salary * savings_percentage / 100

rent = salary * rent_percentage / 100

electricity = salary * electricity_percentage / 100

total_expenses = savings + rent + electricity

remaining = salary - total_expenses

yearly_rent = rent * 12

yearly_electricity = electricity * 12

yearly_rentandelectricity = yearly_rent + yearly_electricity

salary_p2 = salary ** 2

additional_saves = 50

lesft_savingd = additional_saves / savings

print(f"Calculating the expenses for {month}")

print(f"Total savings: {savings}")

print(f"Total rent: {rent}")

print(f"Total electricity: {electricity}")

print(f"Total expenses: {total_expenses}")

print(f"Remaining: {remaining}")

print(f"Yearly rent: {yearly_rent}")

print(f"Yearly electricity: {yearly_electricity}")

print(f"Yearly rent and electricity: {yearly_rentandelectricity}")

print(f"Salary squared: {salary_p2}")

print(f"Additional savings: {additional_saves}")
