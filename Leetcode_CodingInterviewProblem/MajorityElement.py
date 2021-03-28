from collections import Counter
def MajorityElement(numbers):
    count = Counter(numbers)
    for numb in numbers:
        if count.get(numb)>len(numbers)/2:
            return numb
if __name__=="__main__":
    numbers=[1,1,1,3,2,4,1]
    print(MajorityElement(numbers))