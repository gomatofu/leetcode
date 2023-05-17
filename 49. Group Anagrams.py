class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagram = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagram[key].append(s)

        return anagram.values()