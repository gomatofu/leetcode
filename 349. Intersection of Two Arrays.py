class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1 = list(set(nums1))
        nums2 = set(nums2)

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])

        return res