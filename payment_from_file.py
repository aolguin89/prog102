# Init by default payment
payment = None

# Opening the workers file
with open('employees.csv') as file:
    for line in file.readlines()[1:]:
        data = line.split(",")
        if data != ['\n']:
            name = data[0]
            hs = float(data[1])
            rate = float(data[2])
            if hs < 40:
                payment = hs * rate
            else:
                payment = (hs * rate + (hs - 40) * rate * 0.5)

            print("The corresponding paymente for: {} is: {}".format(name, payment))
