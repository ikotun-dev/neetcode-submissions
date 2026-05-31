class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for idx, i in enumerate(nums):
            mul = 1
            for idxj, j in enumerate(nums):
                if idxj != idx:
                    mul = mul*j
            res.append(mul)
        return res

                