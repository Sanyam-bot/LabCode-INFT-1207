import csv
from datetime import date
import os
from sys import exit

# Change working directory to the project root
os.chdir(os.path.dirname(os.path.dirname(__file__)))

MINIMUM_YEAR = 1500

# Function to add a book to the reading list
def add_book(title, author, year):
    today = date.today()  # Get today's date
    if not title or not author or not year: # Making sure title, author and year aren't empty.
        print('Error: The input cannot be empty for title, author, and year.')
        return 1
    try: # Try to cast year to an integer.
        year = int(year)
        if not MINIMUM_YEAR <= year <= today.year: # Making sure the year falls between 1500 and the current year.
            print(f'The year needs to be between 1500 and {today.year}')
            return 1
    except ValueError:
        print("Error: The year input needs to be an integer.")
        return 1
    try:
        with open('src/books.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
            print(f'-- "{title}" successfully written to the csv file.')
    except FileNotFoundError:
        print("Error: The file wasn't found.")
    except PermissionError:
        print("Error: You don't have the permissions to write to the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Function to list all books
def list_books():
    try:
        with open('src/books.csv', mode='r') as file:
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
                exit()

    except FileNotFoundError:
        print("Error: The file wasn't found.")
    except PermissionError:
        print("Error: You don't have the permissions to read this file.")
    except csv.Error as e:
        print(f"Error: CSV format error {e}.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Function to search for a book by title
def search_book(title):
    if not title:
        print('The title cannot be empty.')
        return 1
    try:
        with open('src/books.csv', mode='r') as file:
            reader = csv.reader(file)
            try:
                for row in reader:
                    if row[0].lower() == title.lower():
                        print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                        return
            except IndexError:
                print("Error: Either the file is empty, or the file has empty rows.")
                exit()
            print('Book not found !!!')
            print('Try again')

    except FileNotFoundError:
        print("Error: The file wasn't found.")
    except PermissionError:
        print("Error: You don't have the permissions to read this file.")
    except csv.Error as e:
        print(f"Error: CSV format error {e}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Function to delete a book
def delete_book(title):
    if not title:
        print('The title cannot be empty.')
        return 1
    try:
        with open('src/books.csv', mode='r+', newline='') as file: # The file needs to exist for this.
            reader = csv.reader(file)
            data = list(reader) # Store the data into memory
            writer = csv.writer(file) # Creating a writer object to write to the file.
            try:
                for row in data:
                    if row[0].lower() == title.lower(): # If the book exists, remove it from the list.
                        data.remove(row)
                        print(f"-- Successfully deleted '{row[0]}'")
                        found = True
                        break
                else:
                    found = False
            except IndexError:
                print("Error: Either the file is empty, or the file has empty rows.")

            if not found:
                print("Error: There aren't any records of this book in the file.")

            file.seek(0) # Move the pointer to the top
            file.truncate() # Delete all the entries in the file.
            writer.writerows(data) # Write the updated rows to the file
    except FileNotFoundError: # Exit the program, if the file doesn't exist.
        print("Error: The file wasn't found.")
    except PermissionError:
        print("Error: You don't have the permissions to read this file.")
    except csv.Error as e:
        print(f"Error: CSV format error {e}.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
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
