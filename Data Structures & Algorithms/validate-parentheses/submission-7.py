class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {}
        pairs[')'] = '('
        pairs['}'] = '{'
        pairs[']'] = '['

        for c in s:
            if c in pairs:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

    #basic question we should do

