class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        current=""
        for i in s:
            if i in current:
                ind=current.index(i)
                current=current[ind+1:]
            current+=i
            longest=max(longest,len(current))
        return longest


        
