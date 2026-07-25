class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = {}
        cnt1 = {}
        for i in s:
            cnt[i] = s.count(i)
        for j in t:
            cnt1[j] = t.count(j)

        if cnt == cnt1:
            return True
        else:
            return False