class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        result = set()   
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                if abs(nums[i] - nums[j]) == k:
                    pair = tuple(sorted((nums[i], nums[j])))  
                    
                    result.add(pair)  
        
        return len(result)

        
        
