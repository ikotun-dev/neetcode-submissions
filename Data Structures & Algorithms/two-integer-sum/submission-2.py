class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for idj, j in enumerate(nums):
        #     diff = target - j
        #     for idi, i in enumerate(nums):
        #         if i == diff and idi != idj:
        #             return [idj, idi]
        prevMap = {} #holds the previous vals we checked
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
            
