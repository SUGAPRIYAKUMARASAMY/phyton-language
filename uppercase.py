name=input("enter the string")
count=0
count1=0
for i in name:
    if i.isupper():
        count=count+1
    if i.islower():
        count1=count1+1
print("uppercase:",count)
print("lowercase:",count1)       
        
        
