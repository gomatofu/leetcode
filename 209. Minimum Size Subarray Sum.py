class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cnt = float('Inf')

        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                cnt = min(cnt, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return cnt if cnt != float('inf') else 0