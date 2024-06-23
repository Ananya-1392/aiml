print("Welcome to the tip calculator")
bill = float(input(("What was the total bill? $")))
tip = float(input(("How much tip would you like to give? 10, 12, or 15?")))
number_of_people =int( input(("How many people to split the bill?")))
bill_with_tip = tip / 100 * bill + bill
result = bill_with_tip / number_of_people

final_amount = round(result, 2)
final_amount = "{:.2f}".format(result)
print(f"Each person should pay ${final_amount}")

