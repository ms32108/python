class Solution:
    def largestElement(self, nums):
        nums.sort()
        print(nums)
        return nums[-1]

class Solution:
    def largestElement(self, nums):
        return max(nums)

# taking input
nums = list(map(int, input("Enter numbers: ").split()))

sol = Solution()
print(sol.largestElement(nums))