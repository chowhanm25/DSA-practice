class Solution(object):
    def simplifyPath(self, path):
        lst = path.split('/')
        stack = []
        for d in lst:
            if d == "..":
                if stack:
                    stack.pop()
            elif d != "" and d != ".":
                stack.append(d)
        return "/" + "/".join(stack)
