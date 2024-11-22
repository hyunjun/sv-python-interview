class NumMatrix(object):
    def __init__(self, matrix: List[List[int]]):

        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])
        self.sumM = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                # Sum(ABCD)=Sum(OD)−Sum(OB)−Sum(OC)+Sum(OA)을 구한다.
            self.sumM[i + 1][j + 1] = self.sumM[i][j + 1] + \
                self.sumM[i + 1][j] - self.sumM[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):

        return self.sumM[row2 + 1][col2 + 1] - self.sumM[row2 + 1][col1] - \
            self.sumM[row1][col2 + 1] + self.sumM[row1][col1]
