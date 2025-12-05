books = []
future = []

book_1 = input("Enter the name of a book you own:\n")

books.append(book_1)
book_1 = input("Enter the name of anther book you own (or press 'Enter' to skip ):\n")
if book_1:
    books.append(book_1)
print("\nYour Library: ",books)

book_2 = input("\nEnter the name of a book you wish to have in the future:\n")
future.append(book_2)
book_2 = input("Enter the name of anther book you wish to have (or press 'Enter' to skip):\n")
if book_2:
    future.append(book_2)
print("\nYour Wishlist :",future)

book_3 = input("\nEnter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip):\n")
if book_3:
    books.append(book_3)
    future.remove(book_3)

print("\nUpdated Library: ",books)
print("Updated Wishlist: ",future)

book_4 = input("\nEnter the name of a book from your library you wish to donate (or press 'Enter' to skip):\n")
if book_4:
    books.remove(book_4)

print("\nFinal Library after Donations: ",books)