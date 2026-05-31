class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                #incremement the occurence if it already exists
                hashMap[num] = hashMap[num] + 1
            else:
                hashMap[num] = 1
            
        # return [x for x in hashMap if hashMap[x] >= k]
        return sorted(hashMap, key=lambda x: hashMap[x], reverse=True)[:k]

