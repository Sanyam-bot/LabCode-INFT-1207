import csv
from sys import exit

# Function to add a book to the reading list
def add_book(title, author, year):
    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])


# Function to list all books
def list_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) # skips the first line
        for row in reader:
            print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')


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
                print("There aren't any records of this book in the file.")

            file.seek(0) # Move the pointer to the top
            file.truncate() # Delete all the entries in the file.
            writer.writerows(data) # Write the updated rows to the file
    except FileNotFoundError: # Exit the program, if the file doesn't exist.
        print("There's no file to store and retrieve books.")
        exit(1)

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
