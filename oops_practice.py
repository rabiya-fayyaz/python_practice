class Library:
    def __init__(self, username, books=None):
        self.username = username
        if books is not None:
          self.books = books
        else:
           self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def display_books(self):
       for book in self.books:
          book.display_info()
           
class Book:
    def __init__(self,library,title, author, pages,is_borrowed,rating=None):
        self.library = library
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = is_borrowed
        self.rating = rating

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' by {self.author} is not currently borrowed.")

    def rate_book(self,rating):
        if 1 <= rating <= 5:
            self.rating = rating
            print(f"You have rated '{self.title}' by {self.author} with a rating of {self.rating}.")
        else:
            print("Please provide a rating between 1 and 5.")
            
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        if self.is_borrowed:
          print("Status: Borrowed")
        else:
          print("Status: Available")
        if self.rating is not None:
          print(f"Rating: {self.rating}/5")
        else:
          print("Rating: Not rated yet") 

library1 = Library("Rabiya")
book1 = Book(library1, "The Great Gatsby", "F. Scott Fitzgerald", 180, False)
book1.borrow_book()
book1.return_book()
book1.rate_book(5)
book2 = Book(library1, "To Kill a Mockingbird", "Harper Lee", 281, False)
book2.borrow_book()
book2.return_book()
book2.rate_book(4)
book3 = Book(library1,"Harry potter","J.K Rowling",300,False)
book3.borrow_book()
book3.return_book()
book3.rate_book(4)
library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.display_books()