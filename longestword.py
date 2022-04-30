#longest word
word = "fun&!! time"
length=0
maxlength=0
startindex=0
max_i=0
endindex=0
max_j=0
for i in range(0,len(word)):
    if(word[i].isalpha() or word[i].isnumeric()):
        var=word[i]
        startindex=i
        endindex=i
        length=1

        for j in range(i+1,len(word)):
            if(word[j].isalpha() or word[i].isnumeric()):
                length=length+1
                endindex=j
                if(length>maxlength):
                    maxlength=length
                    max_i=startindex
                    max_j=endindex
            else:
                i=j+1
                break
if(maxlength<length):
    maxlength=length
    max_i=startindex
    max_j=endindex
print(max_i)
print(max_j)
print(maxlength)
print(word[max_i:max_j+1])

