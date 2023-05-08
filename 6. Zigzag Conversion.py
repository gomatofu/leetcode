class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        num,step,ans = 0,0,['']*numRows
        for w in s:
            ans[num] += w
            if num == 0:
                step = 1
            elif num == numRows - 1:
                step = -1
            num += step
        return "".join(ans)
        