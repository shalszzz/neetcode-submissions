class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        # Pacific: top 
        for c in range(cols):
            dfs(0, c, pacific)

        # Pacific: left 
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic: bottom 
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        # Atlantic: right 
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        ans = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans