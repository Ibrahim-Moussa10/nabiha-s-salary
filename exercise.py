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
