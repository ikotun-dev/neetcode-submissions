class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsMap = {}
        for w in strs:
            sw = ''.join(sorted(w))
            if sw in wordsMap:
                wordsMap[sw].append(w)
            else:
                wordsMap[sw] = [w]

        return [val for val in wordsMap.values()]