class Library:
    def __init__(self):
        self.books = [
            {"title": "Book 1", "author": "Author 1", "status": "available"},
            {"title": "Book 2", "author": "Author 2", "status": "available"},
            # 可以继续添加更多的图书
        ]

    def list_books(self):
        print("Available Books:")
        for book in self.books:
            if book["status"] == "available":
                print(f"Title: {book['title']}, Author: {book['author']}")

    def borrow_book(self, title):
        for book in self.books:
            if book["title"] == title and book["status"] == "available":
                book["status"] = "borrowed"
                print(f"Book '{title}' has been borrowed successfully.")
                return
        print(f"Sorry, the book '{title}' is not available or does not exist.")

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title and book["status"] == "borrowed":
                book["status"] = "available"
                print(f"Book '{title}' has been returned successfully.")
                return
        print(f"Sorry, the book '{title}' is not borrowed or does not exist.")


# 创建一个图书馆实例
library = Library()

# 列出所有可借阅的图书
library.list_books()

# 借阅图书
library.borrow_book("Book 1")

# 再次列出所有可借阅的图书（Book 1 应该不在列表中）
library.list_books()

# 归还图书
library.return_book("Book 1")

# 再次列出所有可借阅的图书（Book 1 应该再次出现在列表中）
library.list_books()