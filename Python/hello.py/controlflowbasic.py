class Solution:
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])       # take from first half
            result.append(nums[i + n])   # take from second half
        return result