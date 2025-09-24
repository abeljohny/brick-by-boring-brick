class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


# print(Solution().transpose([[1,2,3],[4,5,6],[7,8,9]]))
# print(Solution().transpose([[1,2,3],[4,5,6]]))
