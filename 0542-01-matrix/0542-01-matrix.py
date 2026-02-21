class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols and mat[new_row][new_col] > mat[row][col] + 1:
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append((new_row, new_col))

        return mat
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # row = len(mat)
        # col = len(mat[0])
        # result = []


        # def dfs(r,c):
        #     count = 1
        #     if r<0 or r>row or c<0 or c>col:
        #         pass
        #     else:
        #         if mat[r][c] == 0:
        #             return count
        #         else:
        #             count += 1
        #             dfs(r - 1, c) 
        #             dfs(r + 1, c) 
        #             dfs(r, c - 1) 
        #             dfs(r, c + 1)


        # for r in range(row):
        #     for c in range(col):
        #         if mat[r][c] == 0:
        #             print(result,"if")
        #             result[r][c] = 0
                    
        #         else:
        #             count = dfs(r,c)
        #             result[r][c] = count
        #             print(result)

        # return result

