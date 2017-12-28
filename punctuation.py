punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_string="hello )$@ sr$%)@i krishna"
no_punc=""
for i in my_string:
    if i not in punctuations:
        no_punc+=i
print(no_punc)
