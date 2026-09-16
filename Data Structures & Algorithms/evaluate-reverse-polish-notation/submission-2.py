class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp = 0
        for token in tokens:
            if token not in ("+","-","*","/"):
                stack.append(int(token))
            elif token in "+-*/":
                if len(stack) < 2:
                    return
                if token == "+":
                    temp = stack[-1] + stack[-2]
                elif token == "-":
                    temp = stack[-2] - stack[-1]
                elif token == "*":
                    temp = stack[-2] * stack[-1]
                elif token == "/":
                    temp = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
        return int(stack[0])
