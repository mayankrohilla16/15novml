
#2							  OUTPUT
print(5**9)                                               # 1953125
print(3//2)						  # 1
print(7//3)						  # 2
print(7/3)						  # 2.3333333333333335
print(6==6)						  # True
a=20;a+=30;a%=3						  
print(a)						  # 2
print(True * False)					  # 0
print(True & False)					  # False
print(True and False)		 		  	  # False
print(((6>3) and (7<4) or (18==3)) and (9>3))		  # False
print(True is False)					  # False
#print(False in 'False')				  # Traceback (most recent call last):
                                                          #   File "C:/Users/ANUJA/Desktop/day6.py", line 13, in <module>
                                                          #  	print(False in 'False')
                                                          # TypeError: 'in <string>' requires string as left operand, not bool

print(((True==False) or (False>True)) and (False<=True))  # False	

#3
s1="Nice to have it"
s2="here"
print(s1+' '+s2)

#4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#5
s1="Nice to have it"
s2="here"

a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

a.insert(0,s1)
a.append(s2)
print(a)

#6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

i=0
while(numbers[i]!=412):
    if numbers[i]%2==0:
        print(numbers[i])
    i=i+1

#7
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#8
string = input('Enter the string')
alphabet='abcdefghijklmnopqrstuvwxyz'
string= string.lower()
flag=0
for i in alphabet:
    if i not in string:
        flag=1
        break
if flag==1:
    print('False')
else:
    print("True")
    


#9
n=int(input('Enter a number'))
print(n+int(str(n)+ str(n))+int(str(n)+ str(n)+ str(n)))

#10

s=input("Enter a string")
l=s.split("#")
list1=l[0].split(' ')
for i in range(len(list1)):
    list1[i]=int(list1[i])
list2=l[1].split(' ')
for i in range(len(list2)):
    list2[i]=int(list2[i])
print(list1)
print(list2)


#11
print("Enter a string: ")
s=input().split(',')
print(s)
s.sort()
print(s)


#12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
d1=d['Marks']
large=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==large):
        j=i

d2=d['Student']
print(d2[j])


#13
#s='hello world! 123'
s=input("Enter a string:")
l=0
d=0
for i in s:
    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("LETTERS ",l)
print("DIGITS ",d)


#14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject: ')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)



#16
import math
x,y=0,0
while True:
    step = input('Type UP,DOWN,LEFT,RIGHT and corresponding Step number:')
    if step == '':
        break
    else:
        step = step.split(' ')
        if step[0]=='UP':
            y+=int(step[1])
        elif step[0]=='DOWN':
            y-=int(step[1])
        elif step[0]=='LEFT':
            x-=int(step[1])
        elif step[0]=='RIGHT':
            x+=int(step[1])
c= math.sqrt(x**2+y**2)
d=int(c)
print('Distance:',d)


