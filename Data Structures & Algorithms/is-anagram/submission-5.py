class Solution:
    def isAnagram(self, S: str, T: str) -> bool:
        if {S[i]: S.count(S[i]) for i in range(len(S))} == {T[i]: T.count(T[i]) for i in range(len(T))}:
            return True
        else:
            return False
        