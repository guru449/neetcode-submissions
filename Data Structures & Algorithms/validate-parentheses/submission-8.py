class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if stack:
                topElement = stack[-1]
                if c == "]":
                    if topElement != "[":
                        return False
                    else:
                        stack.pop()

                elif c == "}":
                    if topElement != "{":
                        return False
                    else:
                        stack.pop()
                elif c == ")":
                    if topElement != "(":
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
            print(stack)
        
        if len(stack) == 0:
            return True
        else:
            return False

