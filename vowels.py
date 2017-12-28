string=input("enter the name")
count=0
for i in string:
    if i in['a','e','i','o','u','A','E','I','O','U']:
        count+=1
print("no of vowels:",count)
