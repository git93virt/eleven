
class library:
    def __init__(self, libBook):
        self.book = libBook

    def displayedbook(self):
        print("books available in this library are: ")
        for book in self.book:
            print(" >" + book)

    def borrowed(self, bookname):
        if bookname in self.book:
            print("your book is ")

    pass


class student:
    def name(self, nam):
        if self.name == nam:
            print(f"welcome {self.name}")

    def Class(self, clas, sec):
        print(
            f"your name is {self.name} and your class {clas} and section is {sec}")
        pass

    def issued_date():
        pass

    def lastSubmitDate():
        pass


if __name__ == "__main__":
    booklist = library(
        ["daredevil", "heman", "harrypotter", "hellincell", "batman"])
    booklist.displayedbook()
