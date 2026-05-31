class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        cleanedText = re.sub(r"[^a-zA-Z0-9]", "", s)

        if cleanedText.lower() == cleanedText.lower()[::-1]:
            return True
        return False
        