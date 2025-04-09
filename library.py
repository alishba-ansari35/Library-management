# Library Management System : 

book_list = list()

# menu items :
menu = """
1) Add Book 
2) Remove Book 
3) View Book 
4) Press E to Exit
"""
# add books
def add_book(booklist, book):
    booklist.append(book)
    print("Book added sucessfully")


# remove books 
def remove_book(booklist, book):
    if booklist not in booklist:
        booklist.remove(book)
        print("Book remove Sucessfully")
    else:
        print("Book not found in this list")



 # display all books result :
def display_list(booklist):
    if booklist:
        print("Added Books -> ", "," .join(booklist))
    else:
        print("No books in the list.")


# Exit program 
def exit_program():
    print("Thankyou for visiting the book library.")
    quit()


# main program loop 
while True:
    print(menu)
    choice = input("Your Choice: ")

    if choice == "1":  # add book
        book_name = input("Enter the book name you wanat to added:")
        add_book(book_list, book_name)



    elif choice == "2": # remove book 
        book_name = input("Enter the book name to remove:")
        remove_book(book_list, book_name)



    elif choice == "3": # view book list
        display_list(book_list)
    

    elif choice .lower() == "e": #exit program
        exit_program()

    else:
        print("Invalid Entry")
        input("Press enter to return main menu!")
