import collections

def is_palindrome_queue(s):

    char_queue = collections.deque()

    for char in s:
        if char.isalnum():
              char_queue.append(char.lower())

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return "Not A Palindrome!"

    return "Palindrome"

name=input("Enter a String:")
print(is_palindrome_queue(name))

