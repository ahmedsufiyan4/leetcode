class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dix1={}
        dix2={}
        for i in s:
            if i not in dix1:
                dix1[i]=1
            else:
                dix1[i]+=1
        for i in t:
            if i not in dix2:
                dix2[i]=1
            else:
                dix2[i]+=1
        if dix1!=dix2:
            return False
        for i in sorted(dix1):
            if dix1[i]!=dix2[i]:
                return(False)
        return(True)
