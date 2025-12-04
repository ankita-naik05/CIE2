import sys

# Price argument
if len(sys.argv) >= 2:
    price = float(sys.argv[1])
else:
    price = 1000

# Tax argument
if len(sys.argv) >= 3:
    tax = float(sys.argv[2])
else:
    tax = 10

print("----- Final Payable Amount -----")
print("Price:", price)
print("Tax:", tax)
print("-------------------------------")
