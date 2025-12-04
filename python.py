import sys

if len(sys.argv) == 3:
    price = float(sys.argv[1])
    tax = float(sys.argv[2])
    print("User provided values")
else:
    print("No input values, using default values")
    price = float(input("Enter the price: "))
    tax = float(input("Enter the tax (%): "))
    

print("----- Final Payable Amount -----")
print("Price:", price)
print("Tax:", tax)
print("-------------------------------")
