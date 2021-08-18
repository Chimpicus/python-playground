print("Savings Calculator!")

user_wage = input("how much do you make per hour? ")
user_hours = input("how many hours do you work per day? ")
user_days = input("how many days do you work per month? ")
user_earnings = round(
    (float(user_wage) * float(user_hours)) * int(user_days), 2)
user_savings = user_earnings / 5
output = round(user_savings, 2)


print("your monthly earnings are: £",user_earnings)
print("your monthly savings should be: £",output)
