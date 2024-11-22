class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        R, C = len(matrix), len(matrix[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, seen):
            if (r, c) in seen:
                return
            seen.add((r, c))
            for nr, nc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                # 다음 지점은 현재 지점보다 높아야 한다.
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] >= matrix[r][c]:
                    dfs(nr, nc, seen)

        for r, c in [(r, 0) for r in range(R)] + [(0, c) for c in range(C)]:
            dfs(r, c, pacific)
        for r, c in [(r, C - 1) for r in range(R)] + [(R - 1, c) for c in range(C)]:
            dfs(r, c, atlantic)
        return pacific & atlantic
