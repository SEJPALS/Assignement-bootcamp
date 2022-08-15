dict1={1:10,2:5,3:15,4:25,5:19}
a=sorted(dict1.values())
print(a)

dict2={0:10,1:20}
dict2[2]=30
print(dict2)

from collections import Counter
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1=Counter(dict1)
dict2=Counter(dict2)
dict3=Counter(dict3)
dict4=dict(dict1+dict2+dict3)
print(dict4)

dict1={"Red":1,"Blue":2,"Green":3}
print(dict1)
for dict_key,dict_value in dict1.items():
    print(dict_key,'->',dict_value)

n=int(input("Enter the values:"))  
z=dict()
for i in range(1,n+1):
    z[i]=i*i
print(z)

dict1={1:10,2:20,3:30}
#del dict1[3]
a=dict1.pop(3)
print(dict1)

lis= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

a=set( val for dic in lis for val in dic.values())
print(a)

from collections import defaultdict,Counter
dict1=input("Enter the string:")
dict2={}
for i in dict1:
    dict2[i]=dict2.get(i,0)+1
print(dict2)

dict1={'Tim':3, 'Kate':2}
print('Name Age')
for name,age in dict1.items():
    print('{} {}'.format(name,age))

data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['success'] for d in data))

dict1={'Science':1,'Maths':2,'English':3}
if all(key in dict1 for key in ('Science', 'Maths','English')):
    print("keys are present")
else:
    print("keys are not present")


li1=[1,3,5,7,9]
dict1=current={}
for i in li1:
    current[i]={}
    current=current[i]
print(dict1)

dict1={'A1':['eggs','bacon','sausage'],'T2':['bread','butter','toast']}
total=0
for value in dict1:
    value_li1=dict[value]
    count=len(value_li)
    total+=count
print(total)



    





