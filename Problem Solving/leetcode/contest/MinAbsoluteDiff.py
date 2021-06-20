import sys


def MinAbsoluteDiff(nums, queries):
    result = []
    for query in queries:
        newNum = nums[query[0]:query[1]+1]
        newNum.sort()
        sol = abs(newNum[1]-newNum[0]) if newNum[1]!=newNum[0] else sys.maxsize
        for i in range(2,len(newNum)):

            if newNum[i]-newNum[i-1]!=0 and abs(newNum[i]-newNum[i-1])<sol:
                sol = abs(newNum[i]-newNum[i-1])
        if not sol:
            result.append(-1)
        else:
            result.append(sol)
    return result