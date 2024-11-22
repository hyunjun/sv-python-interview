# 리스트를 사용하여 큐 구현
# 큐 초기화
queue = []

# 큐에 원소 추가

queue.append("a")
queue.append("b")
queue.append("c")
print("Initial queue")
print(queue)

# 큐에서 원소 제거
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)
