class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if i=="(":
                stack.append("(")
            elif i=="[":
                stack.append("[")
            elif i=="{":
                stack.append("{")
            elif i==")":
                if stack[-1]=="(":
                    stack.pop()
            elif i=="]":
                if stack[-1]=="[":
                    stack.pop()
            elif i=="}":
                if stack[-1]=="{":
                    stack.pop()
        if not stack:
            return True
        else:
            return False
