class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = [1]
        for i in range(1, len(nums)):
            products.append(nums[i - 1] * products[i - 1])

        running_postfix_product = 1
        for i in range(len(nums) - 2, -1, -1):
            running_postfix_product *= nums[i + 1]
            products[i] *= running_postfix_product

        return products