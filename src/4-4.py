class MyCircularQueue:
    def __init__(self, k: int):
        """
        여기에서 데이터 구조를 초기화하고 큐 크기를 k로 설정한다.
        """
        self.data = [0] * k
        self.head = self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        순환 큐에 원소를 삽입한다. 작업이 성공하면 True를 반환한다.
        """
        if self.isFull():
            return False
        self.data[self.tail % len(self.data)] = value
        self.tail += 1
        return True

    def deQueue(self) -> bool:
        """
        순환 큐에서 원소를 제거한다. 작업이 성공하면 True를 반환한다.
        """
        if self.isEmpty():
            return False
        self.head += 1
        return True

    def Front(self) -> int:
        """
        큐에서 맨 앞의 원소를 가져온다.
        """
        if self.isEmpty():
            return -1
        return self.data[self.head % len(self.data)]

    def Rear(self) -> int:
        """
        큐에서 마지막 원소를 가져온다.
        """
        if self.isEmpty():
            return -1
        return self.data[(self.tail - 1) % len(self.data)]

    def isEmpty(self) -> bool:
        """
        순환 큐가 비어 있는지 확인
        """
        return self.head == self.tail

    def isFull(self) -> bool:
        """
        순환 큐가 가득 찼는지 확인
        """
        return self.tail - self.head == len(self.data)
