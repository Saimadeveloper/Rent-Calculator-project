# nput we needs from the  user
# total return
# total food ordered for snacking
# electricity units spend
# charge per Uni
#persons living in rooms/flat

# output
# total amount you have to pay
rent=int(input("Enter your hostel/flat rent="))
food = int(input("Enter the amount of food ordered ="))
electricity_spend= int(input("Enter the total of electricity spend ="))
charge_per_unit=int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in rooms/flats ="))

total_bill= electricity_spend* charge_per_unit
output=(food +rent + total_bill) //persons
print("Each person with pay =", output)


