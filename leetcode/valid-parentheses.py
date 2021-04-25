class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = Stack()
        for ch in s:
            if ch in valids:
                stack.push(valids[ch])
            else:
                if stack.isEmpty():
                    return False
                elif stack.pop() is ch:
                    continue
                else:
                    return False
            
        if stack.isEmpty():
            return True
        return False

    
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        if len(self.data) > 0:
            return False
        return True