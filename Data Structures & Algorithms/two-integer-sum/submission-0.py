class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                result = [prevMap[diff], i]
                return result
            else:
                prevMap[n] = i 
