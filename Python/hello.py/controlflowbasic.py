class Solution:
    def twoSum(self, nums: int, target: int) -> int:
        seen = {}
        
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference],i]
            seen[num] = i
        return[]         
        
                
        
        
        
        
      
    


        