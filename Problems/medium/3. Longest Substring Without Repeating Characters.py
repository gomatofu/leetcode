class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = ""
        max_length = 0
        
        for c in s:
            if c in test:
                test = test[test.index(c)+1:]
            test = test + c
            if max_length < len(test):
                max_length = len(test)
        return max_length