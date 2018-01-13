'''
String : ABCDCDC
Sub string : CDC
output: 2
'''

def count_substring(string, sub_string):
    count=0
    for x in range(len(string)):
        if string[x] in sub_string:
            if (sub_string in string[x:(x+len(sub_string))]):
                count+=1
    return count
