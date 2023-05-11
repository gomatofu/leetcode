class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from itertools import product

        ans = []
        for pro in product(('(', ')'), repeat=n*2):
            cnt = 0
        
            for p in pro:
                if p == '(':
                    cnt+=1
                else:
                    cnt-=1
    
                if cnt < 0:
                    break
            
            if cnt == 0:
                ans.append(''.join(pro))
        return ans