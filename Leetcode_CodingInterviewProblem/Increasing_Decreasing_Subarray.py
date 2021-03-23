def IncreasingDecreasing(list):
    i=0
    while i<len(list) and list[i]<list[i+1]:
        i+=1
    if i==0 or i+1>=len(list):
        return False
    i+=1
    while i<len(list):
        if list[i]>list[i-1]:
            return False
        i+=1
    return True
if __name__=="__main__":
    list =[0,2,3,4,5,2,1]
    print(IncreasingDecreasing(list))