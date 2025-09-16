class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_a = 0

        while l < r:
            w = r - l
            curr_h = min(height[l], height[r])
            curr_a = curr_h * w

            max_a = max(max_a, curr_a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_a
