# import models
from models import (Base, session, 
                    Book, engine)
import datetime
import csv
import time


# Create the main menu - add, search, analysis, exit, view
def menu():
    while True:
        # \n makes the link start on a "new line"
        # \r is basically pressing enter on the keyboard, not necessarily a new line 
        print('''
            \n#### PROGRAMMING BOOKS ####
            \r1) Add Book
            \r2) View All Books
            \r3) Search for Books
            \r4) Book Analysis
            \r5) Exit''')
        choice = input("What would you like to do? ")
        # this is for validating that the input is one of the options we selected
        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input('''Please choose one of the options above.
                  \rA number from 1-5.
                  \rPress enter to try again.''')




# edit books
# delete books
# search books
# data cleaning
def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year,month,day)
    except ValueError:
        input('''
              \n****** DATE ERROR ******
              \rThe date format should include a valid Month Day, Year from the past.
              \rEx: January 13, 2003
              \rPress enter to try again.
              \r************************''')
        return
    else:
        return return_date

# creates a function to turn a string price into a float price and mutate it into an int
def clean_price(price_str):
    try:
        price_float = float(price_str)

    except ValueError:
        input('''
              \n****** PRICE ERROR ******
              \rThe price should be a number without a currency symbol.
              \rEx: 10.99   
              \rPress enter to try again.
              \r************************''')
        return
    else:    
        return int(price_float * 100)
    



def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            # validates if there are any duplicates, and ensures there is only 1 or none
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author,published_date=date, price=price)
                session.add(new_book)
        session.commit()


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add book
            title = input('Title: ')
            author = input('Author: ')
            date_error = True
            while date_error:
                date = input('Published Date (Ex: October 25, 2017): ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            price_error = True
            while price_error:
                price = input("Price (Ex: 25.95): ")
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=author,published_date=date,price=price)
            session.add(new_book)
            session.commit()
            print("Book added")
            time.sleep(1.5)
        elif choice == '2':
            # view books
            for book in session.query(Book):
                print(f"{book.id} | {book.title} | {book.author}")
            input('\nPress enter to return to the main menu.')
            pass
        elif choice == '3':
            # search books
            pass
        elif choice == '4':
            # analysis
            pass
        else:
            print('GOODBYE')
            app_running = False


# this dunder main is used so that when app.py is executed *directly*, it'll run the included functions (in this case, create the engine and then run the app() function automatically on execution)
if __name__ == '__main__':
    # creates all the tables defined by the models associated with a Base object in the database specified by the engine
    Base.metadata.create_all(engine)
    add_csv()
    app()
    

    for book in session.query(Book):
        print(book)
