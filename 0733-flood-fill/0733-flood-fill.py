class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]

        row = len(image)
        col = len(image[0])

        def backtrack(r, c, grid):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if old_color != grid[r][c] or grid[r][c] == color:
                return
            
            grid[r][c] = color

            backtrack(r - 1, c, grid) #adjacent up
            backtrack(r, c - 1, grid) #adjacent left
            backtrack(r + 1, c, grid) #adjacent down
            backtrack(r, c + 1, grid) #adjacent right

        backtrack(sr, sc, image)
        return image