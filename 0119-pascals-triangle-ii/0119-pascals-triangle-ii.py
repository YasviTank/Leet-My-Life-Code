class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        n = rowIndex + 1

        for i in range(1, n):
            temp = [1]
            for j in range(i-1):
                temp.append(result[i-1][j] + result[i-1][j+1])
            temp.append(1)
        

            result.append(temp)
            

        return result[-1]