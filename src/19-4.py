import math


from circle import Circle


# DFS 알고리즘을 사용하는 솔루션
class CircleGroup(object):
    def IsOverlapped(self, circle1, circle2):
        distance = math.sqrt(
            math.pow(circle1.x - circle2.x, 2) +
            math.pow(circle1.y - circle2.y, 2)
        )
        if distance <= (circle1.r + circle2.r):
            return True
        return False

    def ConstructAdjacencyDict(self, circles):
        # 인접한 원을 딕셔너리에 저장한다.
        adjacency_dict = dict()
        for circle1 in circles:
            if circle1 not in adjacency_dict:
                adjacency_dict[circle1] = set()
            for circle2 in circles:
                if circle2 not in adjacency_dict:
                    adjacency_dict[circle2] = set()
                if circle1 != circle2 and self.IsOverlapped(circle1, circle2):
                    adjacency_dict[circle1].add(circle2)
                    adjacency_dict[circle2].add(circle1)
        return adjacency_dict

    def DFS(self, node, adjacency_dict, current_group):
        # 현재 노드를 방문한 경우 이전 노드로 돌아간다.
        if node in current_group:
            return
        current_group.add(node)
        for child_node in adjacency_dict[node]:
            self.DFS(child_node, adjacency_dict, current_group)

    def IsSingleGroup(self, circles) -> bool:
        """원 목록이 주어지면 동일한 그룹에 속하는지 여부를 반환한다."""
        visited = set()
        # 인접 연결 목록을 사용하여 그래프 작성
        adjacency_dict = self.ConstructAdjacencyDict(circles)
        # 깊이 탐색
        self.DFS(circles[0], adjacency_dict, visited)
        # 모든 원을 방문했는지 확인한다.
        return len(visited) == len(circles)
