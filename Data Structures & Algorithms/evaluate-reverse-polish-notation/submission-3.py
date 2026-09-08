class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operands = ["+", "-", "*", "/"]
        stack = []

        for t in tokens:
            if t in operands:
                v1 = stack.pop()
                v2 = stack.pop()
                if t == "+":
                    stack.append(v2  +  v1)
                elif t == "-":
                    stack.append(v2  -  v1)
                elif t == "*":
                    stack.append(v2  *  v1)
                else:
                    stack.append(int(v2  /  v1))
            else:
                stack.append(int(t))
        
        return math.floor(stack[0])
        