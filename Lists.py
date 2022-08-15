li1=[1,2,3,4,5]
total=sum(li1)
print(total)

li2=[1,2,3,4,5]
a=1
for i in li2:
    a=a*i
print(a)

li3=[10,20,30,40]
print(min(li3))

li4=['abc','xyz','aba','1221']
a=0
for i in li4:
    if i[0]==i[-1]:
        print("The words are:",i)
        a=a+1
print("Expeted output:",a)

def final(n):
    return n[-1]
def sort(li5):
    return sorted(li5,key=final)
li5=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sort(li5))

li6=[1,2,3,4,1,5,5,4,3]
c=[*set(li6)]
print(c)

from copy import deepcopy
li1=["Good",[2,4],5.6,9,8]
li=deepcopy(li1)
li[1].append(5)
print(li)

li1=["Morning","Evening","Afternoon"]
li2=["Good","Bad","Average"]
li1.append(li2)
print(li1)

li1=input("Enter strings:")
a=li1.split(" ")
b=[]
n=int(input("Enter the value of n:"))
for i in a:
    if (len(i)>n):
        b.append(i)
print(b)

def final(li1,li2):
    for i in li1:
        for n in li2:
            if i==n:
                a=True
                return a
print(final([1,2,3,4,5],[1,2,3,4,6]))



li1=['Red','Green','White','Black','Pink','Yellow']
newlist=[]
for i in li1:
    if i not in(li1[0],li1[4],li1[5]):
        newlist.append(i)
print(newlist)

from itertools import permutations
li1=list(permutations(range(1,5)))
print(li1)

li2='Hello'
a=list(li2)
print(a)

li1=[1,2,3,4]
li2=[1,2]
s1=set(li1)
s2=set(li2)
s3=s1.difference(s2)
li3=list(s3)
print(li3)

li1=["Red","Green","Yellow"]
li2=["Black","Red","Yellow"]
print(set(li1)& set(li2))





