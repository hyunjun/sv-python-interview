# 큐를 구현하기 위해 collections.deque를 사용한다.
from collections import deque

# 큐 초기화
q = deque()

# 큐에 원소 추가
q.append("a")
q.append("b")
q.append("c")

print("Initial queue")
print(q)

# 큐에서 원소 제거
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)
