def powerSet(numbers):
    subsets = [[]]
    i=0
    while i<len(numbers):
        n = len(subsets)
        j=0
        while j<n:
            subsets.append(subsets[j]+[numbers[i]])
            j+=1
        i+=1
    return subsets
if __name__=="__main__":
    numbers =[1,2,3,4,5]
    result = powerSet(numbers)
    for row in result:
        print(row)