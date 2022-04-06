from re import X


i=0
while i<=5:
    i+=1
    if i%2==0:
        break
    print("*")
    
    vals=[0,1,2]
    vals.insert(0,1)
    del vals[1]
    print(len(vals))
    
    a=1
    b=0
    c=a&b
    d=a|b
    e=a^b
    print(c+d+e)
    
var=0
while var<6:
 var+=1
 if var%2==0:
    continue
print("#")

"""my_list=[[0,1,2,3]for i in range(2)]
print(my_list[2][0])"""

my_list=[i for i in range(-1,2)
    ]
print(len(my_list))
    
var1=1
while var1<10:
    print("#")
    var1=var1<<1
    
my_list_1=[1,2,3]
my_list_2=[]
for v in my_list_1:
    my_list_2.insert(0,v)
    print(my_list_2)
    
for i in range(1):
    print("#")
else:
    print("#")
    
my_list5=[3,1,-2]
print(my_list5[my_list5[-1]])
x=1
x=x==X
list2=[1,2,3,4]
print(list2[-3:-2])

i=0
while i<3:
    i+=2
print("*")

t=[[3-1 for i in range(3)]for j in range(3)]
s=0
for i in range(3):
    s+=t[i][i]
print(s)

my_lst=[1,2,3]
for v in range(len(my_lst)):
    my_lst.insert(1,my_lst[v])
    print(my_lst)