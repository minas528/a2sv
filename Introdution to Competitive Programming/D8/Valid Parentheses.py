class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        
        for c in s:
            if c in {"[", "{", "("}:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                cc = stack.pop() + c
                
                if cc not in {"[]", "()", "{}"}:
                    return False
        
        return not stack
