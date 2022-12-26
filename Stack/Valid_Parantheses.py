class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for c in s:
            if c in {'(','{', '['}:
                stack.append(c)
                continue
            if not stack: return False
            if c == ')':
                if stack[-1]!='(': return False
                stack.pop()
            elif c == '}':
                if stack[-1]!='{': return False
                stack.pop()
            elif c == ']':
                if stack[-1]!='[': return False
                stack.pop()
        if stack: return False
        return True