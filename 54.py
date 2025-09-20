class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:
            # iterate over the first row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # iterate over the rightmost column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # iterate over bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # iterate over left wall
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result