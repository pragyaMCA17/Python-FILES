def insertELE(list1,num):
    '''
    Objective: To insert a number into sorted list at proper position
    Input Parameters: num = number to be inserted
    return : No value
    '''
    # approach : Find the correct idex and insert the number 

    
    length=len(list1)
    
    def addnum(list1,pos):
        if (num < list1[pos]):
            if(pos==0):
                return ([num]+list1[0:])
            else:
                list1= (list1[0:pos]+[num]+(list1[pos:]))
                return list1
        else:
            pos=pos+1
            if (pos!=length):
                return addnum(list1,pos)             #use of recurssion 
            else:
                return list1[:]+[num]
                
    return addnum(list1,pos=0)

def main():
    '''
     objective : To insert a number at correct order in sorted list
     Input parameters :
           list : sorted list
           number : the number which we want to insert
        return value : list after inserting the number
    '''
    
    list1=[int(x) for x in input("Input sorted list :  " ).split()]
    number=int(input("Input the element : " ))
    print("List after inserting : " , insertELE(list1 ,number) )
    
if __name__=='__main__':
    main()    

