from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_balanced(expression):
    matched_brackets = {"}": "{", "]": "[", ")": "("}

    stack = Stack()
    for i in expression:
        if i in matched_brackets.values():
            stack.push(i)

        elif i in matched_brackets:
            if stack.is_empty():
                return False

            elif stack.peek() != matched_brackets[i]:
                return False
            else:
                stack.pop()

    return stack.is_empty()


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
