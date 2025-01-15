class Solution(object):
    def isValid(self, board, x, y, rows, cols, digit, row_sets, col_sets, block_sets):
        # 행 검사
        if digit in row_sets[x]:
            return False

        # 열 검사
        if digit in col_sets[y]:
            return False

        # 3x3 블록 검사
        block_index = (x // 3) * 3 + (y // 3)
        if digit in block_sets[block_index]:
            return False

        return True

    def emptySlots(self, board, rows, cols):
        empty = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    empty.append((i, j))
        return empty

    def DFS(self, board, empty, start, N, rows, cols, row_sets, col_sets, block_sets):
        if start >= N:
            return True

        x, y = empty[start]

        for k in range(1, 10):
            digit = str(k)

            if self.isValid(board, x, y, rows, cols, digit, row_sets, col_sets, block_sets):
                board[x][y] = digit
                row_sets[x].add(digit)
                col_sets[y].add(digit)
                block_sets[(x // 3) * 3 + (y // 3)].add(digit)

                if self.DFS(board, empty, start + 1, N, rows, cols, row_sets, col_sets, block_sets):
                    return True

                # 역추적
                board[x][y] = "."
                row_sets[x].remove(digit)
                col_sets[y].remove(digit)
                block_sets[(x // 3) * 3 + (y // 3)].remove(digit)

        return False

    def solveSudoku(self, board):
        rows = len(board)
        cols = len(board[0])

        empty = self.emptySlots(board, rows, cols)

        # 행, 열, 블록에 대한 set을 준비
        row_sets = [set() for _ in range(rows)]
        col_sets = [set() for _ in range(cols)]
        block_sets = [set() for _ in range(9)]

        # 미리 이미 존재하는 숫자들에 대해 set을 업데이트
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != ".":
                    digit = board[i][j]
                    row_sets[i].add(digit)
                    col_sets[j].add(digit)
                    block_sets[(i // 3) * 3 + (j // 3)].add(digit)

        self.DFS(board, empty, 0, len(empty), rows,
                 cols, row_sets, col_sets, block_sets)
