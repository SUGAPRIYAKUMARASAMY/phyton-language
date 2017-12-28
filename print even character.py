my_str="An apple a day keeps the doctor away"
str=my_str.replace(" ","")
print("accepted string:",str)
resultant_string=str[::2]
print("resultant string:",resultant_string)
expected_string=resultant_string[::-1]
print("expected string:",expected_string)
