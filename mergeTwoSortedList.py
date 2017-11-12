def mergeSortedList(list1,list2,newlist,idx1=0,idx2=0):
    '''
    OBJECTIVE : To make a new sorted list by merging two sorted lists
    INPUT PARAMETERS :
                       1. list1 : sorted list 1
                       2. list2 : sorted list 2
                       3. newlist : new merged list
                       4. idx1 : for traversing list1
                       5. idx2 : for traversing list2
    RETURN VALUE : list3 new sorted list
    '''
    # approach : using recurssion

    if (idx1<=len(list1)-1 and idx2<=len(list2)-1):
        if (len(list1)==0 and len(list2)==0) :
            return newlist
        elif (len(list1)==0 and len(list2)!=0):
            newlist=list2
            return newlist
        elif len(list2)==0 and len(list1)!=0:
            newlist=list1
            return newlist
        else:
            if (list1[idx1]>=list2[idx2]):
                newlist.append(list2[idx2])
                idx2+=1
                return (mergeSortedList(list1,list2,newlist,idx1,idx2))
            else:
                newlist.append(list1[idx1])
                idx1+=1
                return (mergeSortedList(list1,list2,newlist,idx1,idx2))
    else:
        if (idx1==len(list1)):
            newlist=newlist+list2[idx2:]
        elif(idx2==len(list2)):
            newlist=newlist+list1[idx1:]
    return newlist
def main():
    '''
    OBJECTIVE : To make a new sorted list by merging two sorted lists
    INPUT PARAMETERS : NONE
    RETURN VALUE : NONE
    '''
    list1=[int(x) for x in input("LIST1 : ").split()]
    list2=[int(y) for y in input("LIST2 : ").split()]
    newlist=[]
    newlist=mergeSortedList(list1,list2,newlist)
    print("NEW LIST : ",newlist)
    
if __name__== '__main__':
    main()

    
    
            
            
