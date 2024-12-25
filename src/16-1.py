class Solution(object):
    def isValid(self, board, x, y, rows, cols, digit):
        # 열 검사
        for j in range(cols):
            if board[x][j] == digit:
                return False

        # 행 검사
        for i in range(rows):
            if board[i][y] == digit:
                return False

        # 3x3 블록 검사
        boundary_x = x - x % 3
        boundary_y = y - y % 3

        for i in range(boundary_x, boundary_x + 3):
            for j in range(boundary_y, boundary_y + 3):
                if i == x and j == y:
                    continue
                if board[i][j] == digit:
                    return False

        return True

    def emptySlots(self, board, rows, cols):
        empty = []

        # 리스트에 공간의 위치 좌표를 추가한다.
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    empty.append((i, j))

        return empty

    def DFS(self, board, empty, start, N, rows, cols):
        # N은 공백의 수가 된다.
        if start >= N:
            return True

        # 현재 공간의 위치 좌표를 가져온다.
        x = empty[start][0]
        y = empty[start][1]

        # 9개 값을 통해 반복
        for k in range(1, 10):
            # 현잿값이 요구 사항을 충족하는지 확인
            if self.isValid(board, x, y, rows, cols, str(k)):
                board[x][y] = str(k)  # 해당 스도쿠 위치에 값 할당
                if self.DFS(board, empty, start + 1, N, rows, cols):
                    return True
        # 역추적
        board[x][y] = "."
        return False

    def solveSudoku(self, board):
        """
        :type board : list[list[str]]
        :rtype: None 아무것도 반환하지 않고 대신 보드를 제자리에서 수정한다.
        """

        rows = len(board)
        cols = len(board[0])

        empty = self.emptySlots(board, rows, cols)
        self.DFS(board, empty, 0, len(empty), rows, cols)
