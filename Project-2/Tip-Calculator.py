#printing welcome message
print("Welcome to the tip calculator")

#asking for the bill and converting it to float
total_bill = float(input("What was the total bill?\n"))

#asking for the percentage
bill_percentage = float(input("What percentage tip would you like to give?\n"))/100


#asking for how many people
number_people = int(input("How many people to split the bill?\n"))

#calculation
bill_amount_with_tip = total_bill + total_bill*bill_percentage

#rounding to two decimal places
each_person_bill = round(float(bill_amount_with_tip/number_people),2)

#print result with f-string
print(f"Each person should pay: ${each_person_bill}")