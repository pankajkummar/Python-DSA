str = ["2, 5, 10, 11, 7, 12", "2, 7, 8, 9, 10, 11, 15"]
arr1 = str[0].split(", ")
arr2 = str[1].split(", ")
inter = []
#print(arr1)

for number in arr1:
    if number in arr2:
      inter.append(number)
    
          
            
print(inter)   
strArray= ",".join(inter).replace(" ","")
print(strArray)
