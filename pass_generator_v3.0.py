# Library imports
import random
import string
import cryptocode


# Validate the user input according the specifications
def validate_input():
    # Keep asking for input until a valid number is entered
    while True:
        number = input(
            "Enter the desire length of the password, this must be a positive number greater than 7: \n")
        if number.isnumeric() and int(number) > 7:
            return int(number)
        else:
            # Print a error message
            print(
                "Invalid length, the input must be a positive number grater than 7 \n")

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


# Pre: take 2 arguments a file_name to handle, the .txt with the passwords and the app name wich we going to search
# Post: Return a list with 2 elements, the password if exist or an empty string and the number of the line if we have to overwrite


def pass_from_file(file_name, app_name):
    password = ''
    line_num = 0
    res = list()
    file = open(file_name, 'r')
    for line in file.readlines():
        data = line.split(" ")
        if data[0] == app_name:
            password = data[1]
            break
        line_num += 1

    res.append(password.strip())
    res.append(line_num)
    file.close()
    return res

# Save the application and password (previously encrypted) to a file passed by paramenter
# The line number is useful when is necesary make an overwrite


def save_app_pass(file_name, app_name, password, line_num=-1):
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    if line_num >= 0:
        lines[line_num] = app_name + " " + password + "\n"
    else:
        lines.append(app_name + " " + password + "\n")
    file = open(file_name, 'w')
    file.writelines(lines)
    file.close()

# Deploy the menu options and control the logic


def menu(file_name, passkey):
    while True:
        # Print the options
        print("1. Recover a password from file")
        print("2. Generate a new password for an aplication ")
        print("3. Exit")
        selection = input("Enter your selection: \n")
        if selection == "1":
            # Recover, ask for the app name
            app_name = input(
                "Please enter the application for wich you want recover the password (case sensitive)\n")
            pass_list = pass_from_file(file_name, app_name)
            # If exist, print the password
            if pass_list[0] != '':
                # Decrypting
                pwd_decoded = cryptocode.decrypt(pass_list[0].strip(), passkey)
                print("The saved password for {} is: {}".format(
                    app_name, pwd_decoded))
                break
            # There is no saved password for the application
            else:
                print("There is no saved password for the application ")

            # Options if we dont find a pass
            while True:
                print("1. Create a password for the app")
                print("2. Back to main menu")
                # Read the selection
                sub_selection = input("Enter your selection: \n")
                if sub_selection == "1":
                    # Create a new password
                    length = validate_input()
                    pwd = generate_random_string(length)
                    print("The password for the application {} is {}".format(
                        app_name, pwd))
                    # Encrypt and Save to file
                    pwd_encoded = cryptocode.encrypt(pwd, passkey)
                    save_app_pass(file_name, app_name, pwd_encoded)
                    break
                elif sub_selection == "2":
                    break  # Go back to main menu
                else:
                    print("Invalid selection, please try again.")
        elif selection == "2":
            app_name = input(
                "Please enter the application name for which you want to generate a password \n")
            pass_list = pass_from_file(file_name, app_name)
            # If a password already exist, alert the user
            if pass_list[0] != '':
                # Decrypt here
                pwd_decoded = cryptocode.decrypt(pass_list[0].strip(), passkey)
                print("Already exist a saved password for {} is: {}".format(
                    app_name, pwd_decoded))
                while True:
                    print("1. Overwrite")
                    print("2. Back to main menu")
                    # Prompt user for sub-selection
                    sub_selection = input("Enter your selection: \n")
                    if sub_selection == "1":
                        # Create a new password
                        length = validate_input()
                        pwd = generate_random_string(length)
                        print("The new password for the application {} is {}".format(
                            app_name, pwd))
                        # Encrypt and Save to file
                        pwd_encoded = cryptocode.encrypt(pwd, passkey)
                        save_app_pass(file_name, app_name,
                                      pwd_encoded, pass_list[1])
                        break
                    elif sub_selection == "2":
                        break  # Go back to main menu
                    else:
                        print("Invalid selection, please try again.")

            # There is no saved password for the application, create and save
            else:
               # Create a new password
                length = validate_input()
                pwd = generate_random_string(length)
                print("The password for the application {} is {}".format(
                    app_name, pwd))
                # Encrypt and Save to file
                pwd_encoded = cryptocode.encrypt(pwd, passkey)
                save_app_pass(file_name, app_name, pwd_encoded)
                break
        elif selection == "3":
            print("Exiting menu...")
            break  # Exit program
        else:
            print("Invalid selection, please try again.")


file_name = "file.txt"
passkey = "pk"
menu(file_name, passkey)
