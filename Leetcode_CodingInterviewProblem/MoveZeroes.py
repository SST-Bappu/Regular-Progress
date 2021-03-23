def MoveZeroes(list):
    i=count=0
    l = len(list)
    while i<(l-count):
        if list[i]==0:
            list.pop(i)
            list.append(0)
            count+=1
        else:
            i+=1
def MoveZeroes_Optimized(list): #Much Optimized
    j=0
    for item in list:
        if item!=0:
            list[j] = item
            j+=1
    while j<len(list):
        list[j]=0
        j+=1
if __name__=="__main__":
    list=[0,1,0,3,12]
    MoveZeroes_Optimized(list)
    print(list)