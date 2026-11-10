class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        substr = ""
        number = ""
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number = str(stack.pop()) + number
                stack.append(int(number) * substr)
                print(stack)
        result = "".join(stack)

        return result

        