from collections import namedtuple
n=int(input("enter num= "))
Student = namedtuple('student','NAME CLASS ID MARKS')
sum=0
for i in range(n):
      l=[x for x in input().split(' ')]
      s=Student._make(l)
      sum+=float(s.MARKS)
print("%.2f"%round(sum/n,2))
      
      
      

    
