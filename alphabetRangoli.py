'''
To print alphabet rangoli
say size = 5
output :
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

def print_rangoli(size):
    assert 0<size<27
    a="abcdefghijklmnopqrstuvwxyz"
    b=(a[:size])[::-1]   
    dash=(4*size)-3

    # to print first half.......
    for i in range(0,size):
        s=b[:i]+b[i]+(b[:i])[::-1]
        ss="-".join(list(s))
        print(ss.center(dash,"-"))

    #to print second half........
    for i in range (size-2,-1,-1):
        s=b[:i]+b[i]+(b[:i])[::-1]
        ss="-".join(list(s))
        print(ss.center(dash,"-"))
        
def main():
    size=int(input("Enter the size : "))
    print_rangoli(size)

if __name__=="__main__":
    main()

