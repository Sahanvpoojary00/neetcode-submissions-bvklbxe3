class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=list(t)
        if len(s)!=len(t):
            return False
        for i in s:
            if i in l:
                l.remove(i) 
                pass
            else :
                return False

        return True
        
        