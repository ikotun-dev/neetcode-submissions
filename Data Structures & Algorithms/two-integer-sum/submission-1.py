class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idj, j in enumerate(nums):
            diff = target - j
            for idi, i in enumerate(nums):
                if i == diff and idi != idj:
                    return [idj, idi]
