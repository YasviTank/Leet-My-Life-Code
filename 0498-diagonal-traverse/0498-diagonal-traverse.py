class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        m = len(mat)
        n = len(mat[0])
        result = []

        for summ in range(m + n - 1):
            temp = []

            for row in range(m):
                column = summ - row
                # summ = row+column

                if 0<=column<n:
                    temp.append(mat[row][column])

            if summ % 2 == 0:
                temp.reverse()

            result.extend(temp)

        return result


# ANOTHER SOLUTION:

        # key = []

        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if i + j >= len(key):
        #             key.append([])
        #         key[i + j].append(mat[i][j])

        # res = []
        # for i in range(len(key)):
        #     if i % 2 == 0:
        #         res.extend(reversed(key[i]))
        #     else:
        #         res.extend(key[i])

        # return res
        