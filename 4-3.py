# queue.Queue를 사용하여 큐 구현
from queue import Queue

# 큐 초기화
q = Queue(maxsize=3)
# qsize()는 큐 크기를 반환한다.
print(q.qsize())
# 큐에 원소 추가
q.put("a")
q.put("b")
q.put("c")

# 큐가 꽉 찼는지 확인
print("\nFull: ", q.full())

# 큐에서 원소 제거
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# 현재 큐가 비어 있는지 확인
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
