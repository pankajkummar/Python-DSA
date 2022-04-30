#paranthesis using recursion no of combination possible
def parenthesis(n,open,close):
    
    
    if(close==n and open==n):
        return 1
    else:
        if(open>close and open<n):
            return parenthesis(n,open,close+1) + parenthesis(n,open+1,close)
            
        else:
            if(open<n):
                return parenthesis(n,open+1,close)
            else:
                return 1
            

print(parenthesis(3,0,0))



