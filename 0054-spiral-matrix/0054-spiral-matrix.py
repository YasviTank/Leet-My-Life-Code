class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])
        result = []

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            # top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # bottom row (check if still valid)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # left column (check if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result




                