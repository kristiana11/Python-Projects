# display welcome message
print("Welcome to the tip calculator.\n")

# get user input for total bill, how many people to split the bill,
# and what percentage tip 
total_bill = float(input("What was the total Bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? "))
people_split = int(input("How many people to split the bill? "))

######### CALCULATIONS #########

# get overall total
tip_as_percent = percentage_tip / 100
total_tip_amount = total_bill * tip_as_percent
total_amount = total_bill + total_tip_amount
bill_per_person = total_amount / people_split
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

# display answer
print(f"Each person should pay: {final_amount}")
