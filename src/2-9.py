class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        M, N = len(matrix), len(matrix[0])
        self.dp = [[0] * (M + 1) for _ in range(N + 1)]
        for r in range(M):
            for c in range(N):
                self.dp[r][c + 1] = self.dp[r][c] + matrix[r][c]  # 1차원 배열을 사용해 풀기

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1, 1):  # 각 행을 반복하고 각 행에 값을 추가한다.
            sum += self.dp[row][col2 + 1] - self.dp[row][col1]
        return sum
