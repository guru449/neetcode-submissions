class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {}
        pairs[')'] = '('
        pairs['}'] = '{'
        pairs[']'] = '['

        for c in s:
            if c in pairs and len(stack) != 0 and pairs[c] != stack[-1]:
                return False
            elif c in pairs and len(stack) != 0:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        if len(stack) == 0:
            return True
        else:
            return False


