"""
인접 관계를 보여주는 Python 프로그램 그래프의 노드 표현
"""


# 노드 인접 노드의 클래스를 나타낸다.
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# 그래프 클래스, 그래프는 인접 리스트로 구현된다. 배열의 크기는 정점의 수가 된다
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # 무방향 그래프에 간선을 추가하는 기능
    def add_edge(self, src, dest):
        # 소스 노드에 노드 추가
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # 소스 노드를 대상으로 추가
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # 그래프를 출력하는 기능
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# 위의 그래프 클래스의 드라이버
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()
