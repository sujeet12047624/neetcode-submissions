class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''.join(ch for ch in s if ch.isalnum()).lower()
        return res==res[::-1]

        