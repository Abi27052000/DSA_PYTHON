from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(10)

print(q)
print(q.pop())
print(q.pop())
print(q)
