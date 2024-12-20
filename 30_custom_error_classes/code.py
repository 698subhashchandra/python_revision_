class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"Book {self.name}, read {self.pages_read} pages out of {self.pages_count}>"
        )

    def read(self, pages: int):
        self.pages_read += pages
        print(f"You Have Now Read {self.pages_read} pages out of {self.page_count}.")

python101 = Book("Pyhton 101", 100)
python101.read(35)
python101.read(50)
