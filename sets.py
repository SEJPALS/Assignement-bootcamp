set1={"mango","orange","grapes","apple","cherry"}
print(set1)

set2=set("bootcamp")
print("The original set values:"+str(set2))
for i in set2:
    print(i)

a=set()
a.add(10)
print(a)

b=set([1,2,3,4,5])
b.remove(3)
print(b)

c={1,2,3,4,5,6,7,8,9,10}
print("Original set:",c)
c.discard(1)
print("New set:",c)

s1=set([1,2,5,6,7,8])
s2=set([2,5])
print(s2.intersection(s1))

s1={1,2,3,4,5}
s2={6,7,8,9,10}
print(s1.union(s2))

s1={1,2,3,4,5}
s2={5,7,8,9,10,5}
print(s2.difference(s1))

s3={1,2,5,4,7,8}
s4={8,4,1,9,10,5}
print(s4.symmetric_difference(s3))

s5={"A","B","C",5}
s5.clear()
print(s5)

subjects=["Maths","Science","English"]
s6=frozenset(subjects)
print(s6)

s7={1,2,3,4,10}
print("Minimmum value is:",min(s7))
print("Maximum value is:",max(s7))
