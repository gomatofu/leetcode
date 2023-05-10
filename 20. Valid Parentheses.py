class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')': '(', ']':'[', '}': '{'}
        stack = []

        for c in s:
            if c in dict.values():
                stack.append(c)
            elif stack != [] and dict[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []