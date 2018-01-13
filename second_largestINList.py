n = int(input())
arr = list(map(int, input().split()))
assert 2<=n<=10
first, second = 0,0
for x in arr:
    assert -100<=x<=100
    if x>first :
        first,second=x,first
    elif first>x>second :
        second=x
print(second)
            
