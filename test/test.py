def count(arr):
    result=set()
    hash=dict()
    for i in range(1,len(arr)):
        if hash.get(arr[i]):
            k = hash.get(arr[i])
            result.add(k[0])
            result.add(k[1])
        else:
            key = arr[i] + arr[i - 1]
            hash[key]=[i,i-1]


    print(result)
    return len(result)
if __name__=="__main__":
    print(count([1,1,2,3,5,7,8,10]))