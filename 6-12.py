class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.list = deque(maxlen=capacity)
        self.items = {}

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        # 최악의 경우에는 리스트 원소 삭제로 O(n) 시간이 될 수도 있다.
        self.list.remove(key)
        self.list.append(key)
        return self.items[key]

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            # 최악의 경우에는 리스트 원소 삭제로 O(n) 시간이 될 수도 있다.
            self.list.remove(key)
            self.list.append(key)
            self.items[key] = value
            return

        if len(self.items) == self.capacity:
            # deque의 popleft 함수의 시간 복잡도는 O(1)이지만, 리스트에서 최악의 경우 삭제는 O(n)시간이 될 수 있다.
            del self.items[self.list.popleft()]

        self.list.append(key)
        self.items[key] = value
