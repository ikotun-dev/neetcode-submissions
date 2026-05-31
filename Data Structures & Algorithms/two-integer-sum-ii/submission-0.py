class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for idx, num in enumerate(numbers, start=1):
            diff = target - num 
            if diff in prevMap:
                return [prevMap[diff],idx]
            else:
                prevMap[num] = idx

        