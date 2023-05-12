class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ステップ1：kを求める
        k = -1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                k = i
                break
            i -= 1

        # kがなかったら、配列は逆順にソートされているので、反転して終了
        if k == -1:
            nums.reverse()
            return

        # ステップ2：lを求め、nums[k]とnums[l]を入れ替える
        l = k + 1
        i = len(nums) - 1
        while i > k + 1:
            if nums[k] < nums[i]:
                l = i
                break
            i -= 1

        nums[k],nums[l] = nums[l],nums[k]

        # ステップ3：nums[k]より右側の要素を反転させる
        nums[k+1:] = reversed(nums[k+1:])
