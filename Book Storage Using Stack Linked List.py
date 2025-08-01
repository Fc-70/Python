class Node:
    def __init__(self, data):
        self.data = data  # book title
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # top of the stack

    def push(self, book_title):
        new_node = Node(book_title)
        new_node.next = self.top
        self.top = new_node
        print(f'Book "{book_title}" pushed to stack.')

    def pop(self):
        if self.top is None:
            print("Stack is empty! No book to pop.")
            return None
        popped_book = self.top.data
        self.top = self.top.next
        print(f'Book "{popped_book}" popped from stack.')
        return popped_book

    def peek(self):
        if self.top is None:
            print("Stack is empty!")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.top is None:
            print("Stack is empty!")
            return
        current = self.top
        print("Books in stack (top to bottom):")
        while current:
            print(f"- {current.data}")
            current = current.next

# Example Usage

stack = Stack()

while True:
    print("\nLibrary Stack Menu:")
    print("1. Add Book (Push)")
    print("2. Remove Book (Pop)")
    print("3. Peek Top book")
    print("4. Display all books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the book title: ")
        stack.push(title)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        top_book = stack.peek()
        if top_book:
            print(f'Top book is: "{top_book}"')
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
