str1="Good Afternoon","Happy Independence Day","Good Day","Enjoy"
print(len(str1))

from collections import Counter
str2=input("Enter the strings:")
str3=Counter(str2)
print(str3)
#OR
str2=("Enter the strings value:")
dict1={}
for x in str2:
    keys=dict1.keys()
    if x in keys:
        dict1[x]=dict1[x]+1
    else:
        dict1[x]=1
print(dict1)

s1=input(('Enter the string:'))
s3=s1[0]+s1[1:].replace("r","$")
print(s3)

s1=input("Enter the strings:")
if s1.endswith('ing'):
    s1+='ly'
elif len(s1)>=3:
    s1+='ing'
print(s1)

def find_longest_word(word_list):  
    longest_word =  max(word_list, key=len)
    return longest_word
print(find_longest_word(['hello','are','you']))

user=input("Which is your favourite coding language?")
print("My favourite coding language is:",user.upper())
print("My favourite coding language is:",user.lower())

str1=input(("Enter the value of strings:"))
n=int(input("Enter the value of n:"))
print(str1[:n].lower()+str1[n:])

s1=input(('Enter the character:'))
print(s1[::-1])

words=input(("Enter the words:"))
s1=[a for a in words.split(",")]
print(",".join(sorted(list(set(s1)))))

import textwrap
a='''Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.'''
print()
print(textwrap.fill(a,width=50))
print()

a=input(("Enter the strings:"))
print(a.split().pop(0))
print(a.split().pop(-1))

str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])

s1='Today I will learn coding.My favourite coding language is python.'
s2='.'
s3=s1.count(s2)
print(s3)




