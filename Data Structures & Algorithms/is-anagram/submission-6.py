class Solution:
    def isAnagram(self, S: str, T: str) -> bool:
        return {S[i]: S.count(S[i]) for i in range(len(S))} == {T[i]: T.count(T[i]) for i in range(len(T))}
    
      
        