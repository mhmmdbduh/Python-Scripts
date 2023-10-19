class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize the array of all 1s
        answer = [1] * len(nums)
        # Initialize the left and right products
        left = 1
        right = 1
        # Loop through the array
        for i in range(len(nums)):
            # Multiply the current element by the left product
            answer[i] *= left
            # Multiply the current element by the right product
            answer[-1-i] *= right
            # Update the left and right products
            left *= nums[i]
            right *= nums[-1-i]
        return answer

nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))