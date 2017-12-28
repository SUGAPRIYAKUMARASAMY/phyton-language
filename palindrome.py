my_string=input("enter the string")
rev_string=reversed(my_string)
if list(my_string)==list(rev_string):
    print("palindrome")
else:
    print("not an palindrome")
