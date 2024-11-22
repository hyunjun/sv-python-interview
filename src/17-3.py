class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        """
        if not rooms:
            return
        row, col = len(rooms), len(rooms[0])
        # 문의 인덱스 찾기
        q = [(i, j) for i in range(row)
             for j in range(col) if rooms[i][j] == 0]
        for x, y in q:
            # 현재 위치에서 문까지의 거리를 구한다.
            distance = rooms[x][y] + 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                # 문 근처의 빈 방을 찾는다.
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < row
                    and 0 <= new_y < col
                    and rooms[new_x][new_y] == 2147483647
                ):
                    # 업데이트 값
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))
