def TwoSum(numbers,target):
    hash = dict()
    for i in range(len(numbers)):
        if hash.get(numbers[i]):
            return [hash.get(numbers[i])-1,i]
        hash.update({target-numbers[i]: i+1})

if __name__=="__main__":
    numbers = [3,8,7,12,4]
    print(TwoSum(numbers,15))