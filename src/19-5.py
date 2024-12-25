def CountGroups(self, circles: list[Circle]) -> int:
    """원 목록이 주어지면 원 그룹의 수를 반환한다."""
    total_groups = 0
    visited = set()
    adjacency_dict = self.ConstructAdjacencyDict(circles)

    for circle in circles:
        if circle in visited:
            continue
        self.DFS(circle, adjacency_dict, visited)
        total_groups += 1

    return total_groups
