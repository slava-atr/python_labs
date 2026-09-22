import re

TOKEN_PATTERN = re.compile(r"[-+]?\d+(?:\.\d+)?|[+\-*/()]")

class Stack:
    def __init__(self, *args):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])
