# Author: Sanyam Singh Sachdeva and Anchalpreet Kaur
# Student ID: 100963204 and 100960062 respectively
# Description: Generates secure passwords based on user-defined criteria, such as length,
# number of letters, digits, and special characters

import random
import string

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 100
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

# Function to generate a password (skeleton)
def generate_password(length, num_letters, num_digits, num_specials):
    # Ensure total requested characters do not exceed length
    # Generate required characters (letters, digits, specials)
    # Fill remaining characters
    # Shuffle and return password
    pass

# Main function (skeleton)
def main():
    print("\n--- Secure Password Generator ---\n")

    # Step 1: Get user inputs for password length and character distribution

    # Step 2: Validate user inputs

    # Step 3: Generate the password

    # Step 4: Display the generated password

    # Step 5: Save password to file

# Entry point of the script
if __name__ == "__main__":
    main()
