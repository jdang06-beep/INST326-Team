class LibraryItem:
    def __init__(self, title, author, year, copies=1):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.year}) — Copies: {self.copies}"
    @classmethod
    def from_user_input(cls):
        print("\n Add a New Library Item ")
        title = input("Enter the title: ").strip()
        author = input("Enter the author: ").strip()
        year = input("Enter the publication year: ").strip()
        try:
            copies = int(input("Enter number of copies: ").strip())
        except ValueError:
            copies = 1
            print("Invalid input for copies — defaulting to 1.")
        return cls(title, author, year, copies)

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            year=data.get("year"),
            copies=data.get("copies", 1)
        )
class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = []

    def add_item(self, item: LibraryItem):
        self.catalog.append(item)
        print(f"\n'{item.title}' has been added to {self.name} Library!")

    def list_items(self):
        if not self.catalog:
            print("\nThe library catalog is currently empty.")
        else:
            print(f"\n {self.name} Library Catalog ")
            for i, item in enumerate(self.catalog, start=1):
                print(f"{i}. {item}")

    @classmethod
    def from_list(cls, name, items_data):
        lib = cls(name)
        for data in items_data:
            item = LibraryItem.from_dict(data)
            lib.add_item(item)
        return lib
def main():
    my_lib = Library("Campus Library")
    print(f" Welcome to the {my_lib.name} Management System!")

    while True:
        print("\nMenu:")
        print("1. Add a new item")
        print("2. View catalog")
        print("3. Exit")
        choice = input("Enter your choice (1–3): ").strip()

        if choice == "1":
            new_item = LibraryItem.from_user_input()
            my_lib.add_item(new_item)
        elif choice == "2":
            my_lib.list_items()
        elif choice == "3":
            print("\n Exiting the Library Management System. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
  
items = [
    {"title": "Nervous Conditions", "author": "Tsitsi Dangarembga", "year": 1988, "copies": 2},
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "year": 1958, "copies": 1},
]

my_lib_2 = Library.from_list("Campus Library", items)
print(my_lib_2.list_items())


