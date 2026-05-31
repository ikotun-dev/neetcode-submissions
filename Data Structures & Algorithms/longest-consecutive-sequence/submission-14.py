class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sortedList = sorted(set(nums))
        current = 0
        longest = 1
        if len(sortedList) == 0:
            return 0
        for idx in range(len(sortedList)):
            if idx > 0 and sortedList[idx] == sortedList[idx - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest
            
        