import csv
from datetime import date
from sys import exit

MINIMUM_YEAR = 1500

# Function to get a String user input
def get_user_string_input(prompt):
    while True:
        user_input = input(f"{prompt}: ")
        if user_input:
          return user_input # Return the input if it's not empty
        print("Error: The input cannot be empty.")

# Function to get an integer user input
def get_user_input_int(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(f"{prompt}: "))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Error: The input needs to be an integer.")

# Function to add a book to the reading list
def add_book(title, author, year):
    try:
        with open('books.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
    except FileNotFoundError:
        print("Error: The file wasn't found.")
    except PermissionError:
        print("Error: You don't have the permissions to write to the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Function to list all books
def list_books():
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            try:
                next(reader)  # skips the first line
            except StopIteration:
                print("The file is empty.")
                exit()

            try:
                for row in reader:
                    print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
            except IndexError:
                print("Error: Empty row in the file.")

    except FileNotFoundError:
        print("Error: The file wasn't found.")
    except PermissionError:
        print("Error: You don't have the permissions to read this file.")
    except csv.error as e:
        print(f"Error: CSV format error {e}.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Function to search for a book by title
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                return
        print('Book not found')


# Function to delete a book
def delete_book(title):
    try:
        with open('books.csv', mode='r+', newline='') as file: # The file needs to exist for this.
            reader = csv.reader(file)
            data = list(reader) # Store the data into memory
            writer = csv.writer(file) # Creating a writer object to write to the file.
            for row in data:
                if row[0].lower() == title.lower(): # If the book exists, remove it from the list.
                    data.remove(row)
                    found = True
                    break
            else:
                found = False

            if not found:
                print("Error: There aren't any records of this book in the file.")

            file.seek(0) # Move the pointer to the top
            file.truncate() # Delete all the entries in the file.
            writer.writerows(data) # Write the updated rows to the file
    except FileNotFoundError: # Exit the program, if the file doesn't exist.
        print("Error: There's no file to store and retrieve books.")
        exit(1)

# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            today = date.today() # Get today's date
            title = get_user_string_input("Enter book title")
            author = get_user_string_input("Enter author name")
            year = get_user_input_int("Enter year of publication", MINIMUM_YEAR, today.year)
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '4':
            title = input("Enter book title to delete: ")
            delete_book(title)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
