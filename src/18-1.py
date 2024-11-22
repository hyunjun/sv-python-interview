# 무방향 그래프 리스트를 저장하기 위한 Python 데이터 구조
from collections import defaultdict

# 이 클래스는 인접 목록을 사용하여 방향이 지정되지 않은 그래프를 나타낸다.


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # 정점 수
        self.graph = defaultdict(list)  # 그래프를 저장하는 딕셔너리

    # 그래프에 간선을 추가하는 기능
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # 원소의 상위 노드를 찾는 함수 정의
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    # 두 개의 서로 다른 집합을 연결하는 함수 정의
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    # 주어진 그래프에 루프가 포함되어 있는지 확인한다.
    def isCyclic(self):

        # V 하위 집합을 생성하고 모든 하위 집합을 단일 요소 집합으로 초기화하기 위해 메모리를 할당한다.
        parent = [-1]*(self.V)

        # 그래프의 모든 모서리를 탐색하고 각 모서리에 대한 두 꼭짓점의 하위 집합을 찾는다.
    # 두 부분 집합이 동일하면 그래프에 순환이 있다.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


# 그래프 만들기
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
