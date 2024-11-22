from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        pacificSeen = set()
        pacificQueue = deque()
        for y in range(len(matrix)):
            pacificSeen.add((y, 0))
            pacificQueue.append((y, 0))
        for x in range(1, len(matrix[0])):
            pacificSeen.add((0, x))
            pacificQueue.append((0, x))

        atlanticSeen = set()
        atlanticQueue = deque()
        for y in range(len(matrix)):
            atlanticSeen.add((y, len(matrix[0]) - 1))
            atlanticQueue.append((y, len(matrix[0]) - 1))
        for x in range(0, len(matrix[0]) - 1):
            atlanticSeen.add((len(matrix) - 1, x))
            atlanticQueue.append((len(matrix) - 1, x))

        self.bfs(matrix, pacificQueue, pacificSeen)
        self.bfs(matrix, atlanticQueue, atlanticSeen)

        both = pacificSeen & atlanticSeen
        return [list(point) for point in both]

    def bfs(self, matrix, queue, seen):
        while queue:
            y, x = queue.popleft()
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dy, dx in dirs:
                if not (0 <= y + dy < len(matrix)) or not (
                    0 <= x + dx < len(matrix[0])
                ):
                    continue
                if (y + dy, x + dx) in seen:
                    continue
                if matrix[y + dy][x + dx] < matrix[y][x]:
                    continue
                seen.add((y + dy, x + dx))
                queue.append((y + dy, x + dx))
