'''
Write a function called favorite_book() that accepts one parameter, title. The function
should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to include a book
title as an argument in the function call.
'''

def favourite_book(title):
    print (f"One of my recent favourite books is {title}!") 

def main():
    book = input("Enter your favourite book: ")
    favourite_book(book)

main()