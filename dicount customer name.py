
name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")
cost = float(input("Enter cost of purchase: "))

discount = cost * 0.10
total = cost - discount

print("\n--- Bill Details ---")
print("Customer Name:", name)
print("Mobile Number:", mobile)
print("Cost of Purchase:", cost)
print("Discount:", discount)
print("Total Amount to be Paid:", total)
