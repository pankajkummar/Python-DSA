#??? between two number
from operator import truediv


str = "9???1???9???1???9"
Flag= False
for i in range(0,len(str)):
    if(str[i].isnumeric()):
        var1=str[i]
        qmark=0
        for j in range(i+1,len(str)):
            var2=str[j]
            if (str[j] =="?"):
                qmark = qmark+1
            if(str[j].isnumeric()):
                if(int(str[i])+int(str[j])==10 and qmark!=3):
                    Flag=False
                    break
                if(int(str[i])+int(str[j])==10 and qmark==3):
                    Flag=True
                    break
            
                

print(Flag)

            
