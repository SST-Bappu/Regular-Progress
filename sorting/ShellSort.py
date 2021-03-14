def swap(a,b):
    if a>b:
        tmp = a
        a = b
        b = tmp

def ShellSort(list):
    n = len(list)
    gap = n//2
    j =gap
    while j>0:
        i=0
        while i<n:
            if(i+j)>=n:
                break
            if(list[i]>list[i+j]):
                list[i],list[i+j] = list[i+j],list[i]
                k=i-j
                while(k>=0):
                    if(list[k]>list[k+j]):
                        list[k],list[k+j] = list[k+j],list[k]
                    k-=j
            i+=1
        print(f"Gap is = {j} and the list is = {list}")
        j-=1

if __name__=="__main__":
    list = [21,38,29,17,4,25,11,32,9]
    print(list)
    ShellSort(list)
    print(list)