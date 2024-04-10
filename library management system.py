books = ["Twisted love", "Harry Potter", "His prettiest problems", "The Theory of Everything", "Ikigai"]
issued_books = []

def display(books):
    count = 1
    for book in books:
        print(f"{count}. {book}")
        count += 1

def deleteBook(books):
    display(books)
    n = int(input("Enter the id of the book you want to delete: "))

    if 1 <= n <= len(books):
        del books[n - 1]
        print("The book has been deleted successfully!")
    else:
        print("Invalid book ID.")

def issue_book(books, issued_books):
    book = input("Which book would you like to issue? ")
    if book in books:
        books.remove(book)
        issued_books.append(book)
        print("Book '{}' has been issued.".format(book))
    else:
        print("Book '{}' is not available in the library.".format(book))

def add_book(books):
    new_book = input("Enter the name of the book: ")
    books.append(new_book)
    print("Book '{}' has been added.".format(new_book))

def return_book(books, issued_books):
    book = input("Enter the name of the book you want to return: ")
    if book in issued_books:
        issued_books.remove(book)
        books.append(book)
        print(f"Book '{book}' has been returned.")
    else:
        print(f"Book '{book}' is not currently issued.")

while True:
    print("1. Display available books")
    print("2. Add a book")
    print("3. Delete a book")
    print("4. Issue a book")
    print("5. Return a book")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        display(books)
    elif choice == "2":        
        add_book(books)
    elif choice == "3":
        deleteBook(books)
    elif choice == "4":       
        issue_book(books, issued_books)
    elif choice == "5":
        return_book(books, issued_books)
    elif choice == "6":
        print("Thank you for using the library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
