#1
#x=input("Enter your first name:")
#y=input("Enter your last name:")
#print("Hello"+" "+y+" "+x)

#2
#data=input("Enter the values:")
#list=data.split(",")
#tuple=tuple(list)
#print('List:',list)
#print('Tuple:',tuple)

#3
#color_list=["Red","Green","White","Black"]
#x=color_list
#print(x[0],x[-1])

#4
#print(abs.__doc__)
#print(list.__doc__)

#5
#import calendar
#x=int(input("Enter the year:"))
#y=int(input("Enter the month:"))
#print(calendar.month(x,y))

#6
#from datetime import date
#a=date(2014,7,2)
#b=date(2014,7,11)
#c=b-a
#print("Output:",c.days)

#7
#def group_values(data_values,n):
 #   for i in data_values:
  #      if n==i:
   #         return True
    #return False
#print(group_values([1,5,8,3],3))
#print(group_values([1,5,8,3],-1))

#8
#def histogram(values):
 #   for n in values:
        #output=''
        #times=n
        #while(times>0):
            #output+='#'
            #times=times-1
        #print(output)
#histogram([2,3,6,5])

#9
#def concatenate_list(items):
 #   output=''
  #  for i in items:
   #     output+=str(i)
    #return output
#print(concatenate_list([1,5,2,12]))

#10
#import os.path
#f_exists=os.path.exists('readme.txt')
#print(f_exists)

#11
#import os
#print(os.system("dir desktop"))

#12
#import multiprocessing
#print(multiprocessing.cpu_count())

#13
import os
dirPath='C:\\Users\\Jenil\\Desktop'
print(dirPath)
for i in os.listdir(dirPath):
    print(os.path.join(dirPath,i))

#14
import os
print(os.environ)

#15
import getpass
print(getpass.getuser())

#16
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 12
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))


#17
import os
print(os.path.abspath('jpeg'))

#18
import os.path, time
file="Tableau notes.txt"
print("Modified:",time.ctime(os.path.getmtime(file)))
print("Created:",time.ctime(os.path.getctime(file)))

#19
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))

a=min(x,y,z)
b=max(x,y,z)
c=(x+y+z)-a-b
print("Number in sorted manner:",a,b,c)

#20
