class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        length = len(nums)

        def traverse(comb,start_index):
            output.append(comb[:])

            for i in range(start_index,length):
                comb.append(nums[i])
                traverse(comb,i+1)
                comb.pop()

        traverse([],0)
        return output