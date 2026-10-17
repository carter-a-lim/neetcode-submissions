class Solution:
    def isValid(self, s: str) -> bool:
        pars = { '(':')', '{':'}', '[':']'}
        stack = []

        for char in s:
            if char in pars:
                stack.append(char)
                continue

            #end bracket char
            if len(stack) > 0 and pars[stack[-1]] == char:
                stack.pop()
            else:
                return False

        if len(stack) > 0:
            return False

        return True
