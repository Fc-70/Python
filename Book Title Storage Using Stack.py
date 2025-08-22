class BookStack:
    def __init__(self, capacity):
        self.stack = [] 
        self.capacity = capacity

    def push(self, title):
        if len(self.stack) >= self.capacity:
            print("Stack Overflow! Cannot add more books.")
        else:
            self.stack.append(title)
            print(f'Book "{title}" added to the stack.')

    def pop(self):
        if not self.stack:
            print("Stack Underflow! No books to remove.")
        else:
            removed = self.stack.pop()
            print(f'Book "{removed}" removed from the stack.')

    def peek(self):
        if not self.stack:
            print("Stack is empty. Nothing to peek.")
        else:
            print(f'Top book in the stack: "{self.stack[-1]}"')

    def display(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("Books in the stack (top to bottom):")
            for book in reversed(self.stack):
                print(f' - {book}')


def main():
    max_books = int(input("Enter the maximum number of books the stack can hold: "))
    book_stack = BookStack(max_books)

    while True:
        print("\nStack Operations Menu:")
        print("1. Add Book (Push)")
        print("2. Remove Book (Pop)")
        print("3. Peek Top Book")
        print("4. Display Stack")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title to add: ")
            book_stack.push(title)
        elif choice == '2':
            book_stack.pop()
        elif choice == '3':
            book_stack.peek()
        elif choice == '4':
            book_stack.display()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
