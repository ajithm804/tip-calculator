bill_total = float(input("Grand total of the bill? "))
tip = int(input("What percentage tip like you would to give? "))
total_members = int(input("How many people would be splitting the bill? "))
tip_percentage = tip/100
tip_total = bill_total * tip_percentage
grand_total_with_tip = bill_total + tip_total
bill_per_person = grand_total_with_tip/total_members
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")