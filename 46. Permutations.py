class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools

        ans = []        
        p = itertools.permutations(nums)

        for v in p:
            ans.append(list(v))

        return ans