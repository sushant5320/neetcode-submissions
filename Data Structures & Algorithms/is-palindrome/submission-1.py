class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm_str = ''
        for i in s[:]:
            if i.isalnum():
                norm_str += i

        revrt_str = ''
        for i in s[:][::-1]:
            if i.isalnum():
                revrt_str += i

        return str.lower(norm_str) == str.lower(revrt_str)