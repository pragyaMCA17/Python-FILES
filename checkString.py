'''
to check if input string has any alphanum,digit, alphabet,lower,upper case in it
ex: s = "123"

'''

if __name__ == '__main__':
    s = input()
    print(any(filter(str.isalnum,s)))
    print(any(filter(str.isalpha,s)))
    print(any(filter(str.isdigit,s)))
    print(any(filter(str.islower,s)))
    print(any(filter(str.isupper,s)))
