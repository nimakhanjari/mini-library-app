from library.library_manager import LibraryManager


def show_menu():
    print("\nMini Library App")
    print("1. Add book")
    print("2. List books")
    print("3. Search book by title")
    print("4. Delete book by ID")
    print("5. Exit")


def main():
    manager = LibraryManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            manager.add_book(title, author, year)
            print("✅ Book added successfully.")

        elif choice == "2":
            books = manager.list_books()
            if not books:
                print("No books in library.")
            else:
                for b in books:
                    print(f'{b["id"]}. {b["title"]} - {b["author"]} ({b["year"]})')

        elif choice == "3":
            keyword = input("Enter title keyword: ")
            results = manager.search_by_title(keyword)
            if not results:
                print("No matching books found.")
            else:
                for b in results:
                    print(f'{b["id"]}. {b["title"]} - {b["author"]} ({b["year"]})')

        elif choice == "4":
            book_id = int(input("Enter book ID to delete: "))
            manager.remove_by_id(book_id)
            print("🗑 Book removed.")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
