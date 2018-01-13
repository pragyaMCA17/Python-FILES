''' print marks of second lowest student in alphabetical order
'''
student={}
for _ in range(int(input())):
    name = input()
    score = float(input())
    student[name]=score
first,second=100000000,100000000
for x in student.values():
    if x<first:
        first,second=x,first
    elif first<x<second :
        second = x
name_min=sorted([name for name,score in student.items() if (score==second)])
for z in name_min:
    print(z)
