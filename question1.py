class Book:
    pass

Harry_Potter = Book()
Harry_Potter.title = 'Harry Potter'
Harry_Potter.author = 'J. K. Rowling'
Harry_Potter.genre = 'Fantasy'
Harry_Potter.year_of_publish = 1997
Harry_Potter.no_of_pages = 572

Winnie_the_Pooh = Book()
Winnie_the_Pooh.__dict__['title'] = 'Winnie-the-Pooh'
Winnie_the_Pooh.__dict__['author'] = 'A. A. Milne'
Winnie_the_Pooh.__dict__['genre'] = 'Children\'s literature'
Winnie_the_Pooh.__dict__['year_of_publish'] = 1926
Winnie_the_Pooh.__dict__['no_of_pages'] = 200

Narnia = Book()
Narnia.title = 'Narnia'
Narnia.author = 'C. S. Lewis'
Narnia.genre = 'Fantasy'
Narnia.year_of_publish = 1950
Narnia.no_of_pages = 623

def create_book(title, author, genre, year_of_publish, no_of_pages):
    new_book = Book()
    new_book.title = title
    new_book.author = author
    new_book.year_of_publish = year_of_publish
    new_book.genre = genre
    new_book.no_of_pages = no_of_pages
    return new_book

print(create_book('newbook', 'liza', 'fantasy', 2021, 105).__dict__)


list_of_books =[Harry_Potter, Winnie_the_Pooh, Narnia]

books_dictionary = {}
books_dictionary[Book.]