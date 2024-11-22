# Array 중 에서 k개 원소를 무작위로 선택한다.
import random


# Array를 인쇄하는 함수 구현
def printArray(stream, n):
    for i in range(n):
        print(stream[i], end=" ")
    print()


# Array [0..n-1]에서 k 개의 원소를 무작위로 추출하는 함수 구현
def selectKItems(stream, n, k):
    i = 0
    # reservoir[]는 stream[]의 k개 원소 길이의 0으로 초기화된 배열
    reservoir = [0] * k
    for i in range(k):
        reservoir[i] = stream[i]

        # (k + 1)번째 원소부터 n번째 원소까지 반복한다.
        while i < n:
            # 0부터 i까지의 원소 중 임의의 인덱스를 선택한다.
            j = random.randrange(i + 1)
            # 무작위로 선택한 인덱스가 k보다 작으면 인덱스의 원소를 stream의 새 원소로 바꾼다.
            if j < k:
                reservoir[j] = stream[i]
            i += 1
        print("Following are k randomly selected items")
    printArray(reservoir, k)
    # main 함수
    if __name__ == "__main__":
        stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        n = len(stream)
        k = 5
        selectKItems(stream, n, k)
