books = [
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
{"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
{"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
{"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]
print("1.	Add a new book\n2.	Remove a book\n3.	Search for a book by title\n4.	Search for a book by author (optional)\n5.	List all the books\n6.	Quit")


def add():
    titlename=input("Enter the title of the book you want to add: ")
    print()
    author=input("Enter the name of the author: ")
    print()
    year=int(input("Enter the year in which the book was published: "))
    print()
    newdict={"title": titlename, "author": author, "year":year}
    books.append(newdict)
    print(f"{titlename} book by author {author} published in year {year} has been added in the dictionary list")
    


def rem():
    rem_title = input("Enter the name of the book to remove: ")
    found = False
    for book in books:
        if book["title"].lower() == rem_title.lower():
            books.remove(book)
            print(f"{rem_title} has been removed from the list.")
            found = True
            break
    if not found:
        print(f"{rem_title} is not in the list.")
  

    
    
def search_by_title():
    title= input("Enter the title of the book: ")
    found =False
    for book in books:
        if book["title"].lower()== title.lower():
            print(f"{title} book by author {book["author"]} published in year {book["year"]} is in the library")
            found=True
    if not found:
        print(f"{title} is not in the list of dictionaries")

def search_by_author():
    author= input("Enter the author of the book: ")
    found =False
    for book in books:
        if book["author"].lower()== author.lower():
            print(f"{book["title"]} book by author {book["author"]} published in year {book["year"]} is in the library")
            found=True
    if not found:
        print(f"{author} is not in the list of dictionaries")

def list_of_books():
    
    print("The list of books are")
    print("=============================================================")
    for book in books:
        print(f"{book.get("title")}")
       
        
while True:
    userchoice=int(input("Enter a choice from the menu(1/2/3/4/5/6):: "))
    
    if userchoice==1:
        add()
    elif userchoice==2:
        rem()
    elif userchoice==3:
        search_by_title()
    elif userchoice==4:
        search_by_author()
    elif userchoice==5:
        list_of_books()
    elif userchoice==6:
        break    
    else:
        print("Enter between 1-6 from the menu")
    