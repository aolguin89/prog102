# asking for data
hs = int(input("Enter the hours worked "))
rate = int(input("Enter employee rate "))

# Init by default payment
payment = None

if hs < 40:
    payment = hs * rate
else:
    payment = (hs * rate + (hs - 40) * rate * 0.5)

print("The corresponding payment is: ", payment)
