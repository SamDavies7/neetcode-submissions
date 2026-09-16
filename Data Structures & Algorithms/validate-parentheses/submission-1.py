class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif len(stack) < 1:
                return False
            elif char in "}])":
                if stack[-1] == "(" and char == ")":
                    stack.pop(-1)
                elif stack[-1] == "[" and char == "]":
                    stack.pop(-1)
                elif stack[-1] == "{" and char == "}":
                    stack.pop(-1)
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
