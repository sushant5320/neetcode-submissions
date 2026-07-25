class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = {i:s.count(i) for i in s}
        cnt1 = {j:t.count(j) for j in t}
        if cnt == cnt1:
            return True
        else:
            return False
        