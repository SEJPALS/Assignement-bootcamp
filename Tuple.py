t1=("Learning","Coding","Good")
print(t1)
#empty tuple
t2=()
print(t2)

t2=("Data Science",2,True,9.8)
print(t2)

t3=("SFIT",10,"Engineering")
(college_name,stud_id,degree)=t3
print(college_name)
print(stud_id)
print(degree)

from copy import deepcopy
t4=("Hello",4,[2,3,4],True,10.0)
print(t4)
t5=deepcopy(t4)
t5[2].append(5)
print(t5)
print(t4)

tup=(1,3,4,32,1,1,1,31,32,12,21,2,3)
for i in tup:
    if tup.count(i) > 1:
        print(i)

def tup_1(values,n):
    for i in values:
        if n==i:
            return True
    return False
print(tup_1([1,2,3,4,5],3))

t1=[1,2,3,4,5]
t2=tuple(t1)
print(t2)

#tuples are immutable so we not change or modify
t1=(1,4,5,7,8,9)
print(t1)
t1=t1[:2]+t1[3:]
print(t1)

t1=(2,3,5,7,9,11)
print(t1)
t2=t1[3::]
print(t2)

t3=(10,20,20,50)
print(t3)
t4=t3[::-1]
print(t4)















