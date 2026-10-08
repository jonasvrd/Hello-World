# Jonas von Ruden-Doll
# 09/10/2026
# Homework 1

# Sales Tax Calculator
# item_price= float(input("How much did the item cost?"))
# item_quantity= int(input("How many items did you order?"))
# sales_tax= 1.075
# subtotal= item_price * item_quantity
# final_price= subtotal * sales_tax
# tax_amount= final_price - subtotal
# print("The subtotal is $",round(subtotal,2))
# print("The amount of tax is $",round(tax_amount,2))
# print("The final price is $",round(final_price,2))

# Employee Weekly Pay Calculator
# total_hours= float(input("How many hours did you work this week in total?"))
# hourly_wage= float(input("How much is your wage hourly?"))
# if total_hours > 40:
#     base_hours = 40
#     overtime_hours = total_hours - 40
#     print("Employee is eligible for overtime pay.")
# else:
#     base_hours = total_hours
#     overtime_hours = 0
#     print("No overtime worked.")
# base_pay= base_hours * hourly_wage
# overtime_pay= overtime_hours * (hourly_wage *1.5)
# total_pay= overtime_pay + base_pay
# print("Base pay is $",round(base_pay,2))
# print("Overtime pay is $",round(overtime_pay,2))
# print("Total pay is $",round(total_pay,2))

# Student Grade Catergorizor
# grade= int(input("What numeric grade did you recieve? "))
# if grade < 60:
#     print("The letter grade you recived is: F")
# elif grade <= 69:
#     print("The letter grade you recived is: D")
# elif grade <= 79:
#     print("The letter grade you recived is: C")
# elif grade <= 89:
#     print("The letter grade you recived is: B")
# elif grade <=100:
#     print("The letter grade you recived is: A")
# else:
#     print("You cannot recieve a grade for this input")
# Boundary test for each letter grade

# Bonus Eligibility Checker
# hours_worked = float(input("Enter total hours worked this week: "))
# performance_score = float(input("Enter performance score: "))
# if hours_worked > 35 and performance_score > 85:
#     print("Congratulations! You are eligible for a bonus!")
# else:
#     print("You are not eligible for a bonus.")
# if hours_worked <= 35:
#     hours_needed = 35 - hours_worked
#     print("You need to work this many more hours to qualify for a bonus",hours_needed)
# if performance_score <= 85:
#         points_needed = 85 - performance_score
#         print("You need this many more performance points to qualify for a bonus:",points_needed)
