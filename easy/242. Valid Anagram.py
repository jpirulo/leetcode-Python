class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        if len(s) != len(t):
            return False
        else:
            if sorted(s1)==sorted(t1):
                return True
            else:
                return False