class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1,d2={},{}
        for a in s:
            if a in d1:
                d1[a]+=1
            else:
                d1[a]=1
        for a in t:
            if a in d2:
                d2[a]+=1
            else:
                d2[a]=1
        print(d1,d2)
        return d1==d2
            
            
        