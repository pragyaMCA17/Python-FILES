'''
to print dec , octal , hex(in capital) , binary form of number
'''

def print_formatted(number):
        for i in range(1,number+1):
        print(str(i).rjust(len("{0:b}".format(number))),"{0:o}".format(i).rjust(len("{0:b}".format(number))),("{0:x}".format(i)).upper().rjust(len("{0:b}".format(number))),"{0:b}".format(i).rjust(len("{0:b}".format(number))))
        
