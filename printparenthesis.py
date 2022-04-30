#print parenthesis
#paranthesis using recursion no of combination possible
from inspect import stack



stack = []
res = []
def parenthesis(n,open,close):
    
    
    if(close==n and open==n):
        res.append("".join(stack))
        return 1
    if open<n:
        stack.append("(")
        parenthesis(n,open+1,close)
        stack.pop()
    if close<open:
        stack.append(")")
        parenthesis(n,open,close+1)
        stack.pop()

print(parenthesis(4,0,0))
print(len(res),res)


