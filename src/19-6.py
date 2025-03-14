from circle import Circle
import heapq


def GetTopKGroups(self, circles: list[Circle], top_k: int) -> list[list[Circle]]:
    """원 목록이 주어지면 가장 큰 k개의 원 그룹을 반환한다."""
    visited = set()
    size_and_groups = []
    adjacency_dict = self.ConstructAdjacencyDict(circles)

    for circle in circles:
        if circle in visited:
            continue
        current_group = set()
        self.DFS(circle, adjacency_dict, current_group)
        size_and_groups.append((len(current_group), current_group))
        visited = visited.union(current_group)

    return [list(group) for _, group in heapq.nlargest(top_k, size_and_groups)]
