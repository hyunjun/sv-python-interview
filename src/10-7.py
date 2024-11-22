# 이진 인덱스 트리의 Python 구현
# arr [0,…,index]의 합을 반환한다. 이 함수는 배열이 전처리되었다고 가정한다.
# 배열 원소의 부분합을 BITree []에 저장한다.
def getsum(BITree, i):
    s = 0  # 합계 초기화
    # BITree[]의 인덱스는 arr[]의 인덱스보다 1이 크기 때문에 i+1을 수행한다.
    i = i + 1
    # BITree의 조상 노드 순회
    while i > 0:
        # BITree에 현재 원소 추가
        s += BITree[i]
        # 현재 인덱스 값을 부모 노드로 이동
        i -= i & (-i)
    return s


# 주어진 인덱스에서 BITree의 노드를 업데이트한다.
# 주어진 값 val이 BITree[i] 및 모든 조상 트리에 추가된다.


def updatebit(BITree, n, i, v):
    # BITree []의 인덱스는 arr []의 인덱스보다 1 더 크다.
    i += 1
    # 모든 조상을 탐색하여 val을 추가한다.
    while i <= n:
        # BITree의 현재 노드에 val을 추가한다.
        BITree[i] += v
        # 인덱스를 상위 인덱스로 업데이트한다.
        i += i & (-i)


# 주어진 크기 n 배열에 대한 BITree를 구성하고 반환한다.


def construct(arr, n):
    # BITree []를 생성하고 0으로 초기화한다.
    BITree = [0] * (n + 1)
    # 업데이트()를 사용하여 BITree[]에 실제 값을 저장한다.
    for i in range(n):
        updatebit(BITree, n, i, arr[i])
    return BITree


# 테스트 코드 부분
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITree = construct(freq, len(freq))
print("Sum of elements in arr[0..5] is " + str(getsum(BITree, 5)))
freq[3] += 6
updatebit(BITree, len(freq), 3, 6)
print("Sum of elements in arr[0..5] after update is " + str(getsum(BITree, 5)))
