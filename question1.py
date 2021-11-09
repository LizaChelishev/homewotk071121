class Book:
    pass


Harry_Potter = Book()
Harry_Potter.title = 'Harry Potter'
Harry_Potter.author = '	J. K. Rowling'
Harry_Potter.genre = 'Fantasy'
Harry_Potter.__dict__['year_of_publish'] = 1997
Harry_Potter.no_of_pages = 572


def create_book(title, author, genre, year_of_publish, no_of_pages):
    new_book = Book()
    new_book.title = title
    new_book.author = author
    new_book.year_of_publish = year_of_publish
    new_book.genre = genre
    return new_book