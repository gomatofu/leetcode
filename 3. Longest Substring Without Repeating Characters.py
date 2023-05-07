class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()
        max_len = 0
        i,j,n = 0,0,len(s)

        while i < n and j < n:
            if s[j] not in w:
                w.add(s[j])
                max_len = max(len(w),max_len)
                j+=1
            else:
                w.discard(s[i])
                i+=1
        return max_len
