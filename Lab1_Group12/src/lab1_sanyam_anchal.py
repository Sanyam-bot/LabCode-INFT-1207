# Author: Sanyam Singh Sachdeva and Anchalpreet Kaur
# Student ID: 100963204 and 100960062 respectively
# Description: Generates secure passwords based on user-defined criteria, such as length,
# number of letters, digits, and special characters

import random
import string

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 1000
MIN_LETTERS_LENGTH = 2
MIN_DIGITS_LENGTH = 1
MIN_SPECIAL_CHARACTERS_LENGTH = 1

# Function to get user input
def get_user_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(f"{prompt}: "))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a value between {min_value} and {max_value}, inclusive, to create a secure password.")
        except ValueError:
            print("The input needs to be an integer.")

# Function to generate a password
def generate_password(letters_length, digits_length, special_character_length):
    # Generate required characters (letters, digits, specials)
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase)
    ]

    for _ in range(letters_length - 2):
        password.append(random.choice(string.ascii_letters))

    for _ in range(digits_length):
        password.append(random.choice(string.digits))

    for _ in range(special_character_length):
        password.append(random.choice(string.punctuation))

    # Shuffle
    random.shuffle(password)

    # Join the password into a string
    password_string = "".join(password)

    # Return password
    return password_string

# Main function (skeleton)
def main():
    print("\n--- Secure Password Generator ---\n")

    # Step 1: Get user inputs for password length and character distribution.

    valid_input = False
    while not valid_input:
        total_length = get_user_input("Enter the total length of the password: ", PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH)
        letters_length = get_user_input("Enter the number of letters desired in the password: ", MIN_LETTERS_LENGTH, PASSWORD_MAX_LENGTH)
        digits_length = get_user_input("Enter the number of digits desired in the password: ", MIN_DIGITS_LENGTH, PASSWORD_MAX_LENGTH)
        special_character_length = get_user_input("Enter the number of special characters desired in the password: ", MIN_SPECIAL_CHARACTERS_LENGTH, PASSWORD_MAX_LENGTH)

        # Step 2: Validate user inputs
        if total_length < (letters_length + digits_length + special_character_length):
            print("The sum of letters, digits, and special characters exceeds the total length. Please enter the valid length for letters, digits and special characters.\n")
        else:
            valid_input = True

    # Step 3: Generate the password
    password = generate_password(letters_length, digits_length, special_character_length)

    # Step 4: Display the generated password
    print(f"Your desired password is: {password}")
    print("Password successfully generated with:")
    print(f" - Letter: {letters_length}")
    print(f" - Digits: {digits_length}")
    print(f" - Special Characters: {special_character_length}")

    # Step 5: Save password to file
    try:
        with open("output.txt", "w") as file:
            file.write(f"Password: {password}\n")
    except PermissionError:
        print("Error: Permission denied")
    except OSError:
        print(f"OSError: {OSError}")

    print("\nResults saved to Output.txt")


# Entry point of the script
if __name__ == "__main__":
    main()