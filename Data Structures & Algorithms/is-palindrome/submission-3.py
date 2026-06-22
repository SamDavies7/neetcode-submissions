class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower()
        cleaned = ""
        for char in lowerS:
            if char.isalnum():
                cleaned += char
        return cleaned == cleaned[::-1]