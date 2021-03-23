def WaterContainer(list):
    i = 0
    j = len(list)-1
    MaxContainer = 0
    while i<j:
        MaxContainer=max(MaxContainer,min(list[i],list[j])*(j-i))
        if list[i]>list[j]:
            j-=1
        else:
            i+=1
    return MaxContainer
if __name__=="__main__":
    list = [1,2,1]
    print(WaterContainer(list))