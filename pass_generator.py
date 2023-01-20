# Library imports
import random
import string


# Validate the user input according the specifications
def validate_input():
    # Keep asking for input until a valid number is entered
    while True:
        number = input(
            "Enter the desire length of the password, this must be a positive number greater than 2: \n")
        if number.isnumeric() and int(number) > 2:
            return int(number)
        else:
            # Print a error message
            print(
                "Invalid length, the input must be a positive number grater than 2 \n")

# Generates a random string with at least a lowercase letter, an uppercase letter and a digit


def generate_random_string(length):

    # Generate a random lowercase letter
    random_lowercase_letter = random.choice(string.ascii_lowercase)

    # Generate a random uppercase letter
    random_uppercase_letter = random.choice(string.ascii_uppercase)

    # Generate a random number
    random_number = random.choice(string.digits)

    # Combine the random lowercase letter, uppercase letter, and number
    random_string = random_lowercase_letter + \
        random_uppercase_letter + random_number
    random_char_list = list(random_string)

    # Append the rest of the characters
    for i in range(length - 3):
        random_char_list.append(random.choice(
            string.ascii_letters + string.digits))

    # shuffle to garantize a random format
    random.shuffle(random_char_list)

    # finally return the list as a string
    return ''.join(random_char_list)


app_name = input(
    "Welcome, please enter the application name for which you want to generate a password \n")
length = validate_input()
print("The password for the application {} is {}".format(app_name,
                                                         generate_random_string(length)))
