class Chapter:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

class Book:
    def __init__(self, title, chapters):
        self.title = title
        self.chapters = chapters

    def total_pages(self):
        return sum(chapter.pages for chapter in self.chapters)

book_chapters = [ Chapter("Chapter 0", 10), Chapter("Chapter 1", 25), Chapter("Chapter 2", 50) ]

book = Book("The Debadarshi", book_chapters)

print(f"Total pages in the book '{book.title}': {book.total_pages()}")