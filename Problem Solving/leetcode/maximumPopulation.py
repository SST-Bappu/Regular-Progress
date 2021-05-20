def maxPopulation(logs):
    logs.sort()
    print(logs)
    left = 0
    right = left+1
    max = 1
    earliest = logs[left][0]
    while left<len(logs):
        count =1
        while right<len(logs) and logs[right][0]<logs[left][1]:
            count+=1
            r = right - 1
            c = count
            while r>left:
                if logs[right][0]>=logs[r][1]:
                    c-=1
                r-=1
            if c>max:
                max = c
                year = logs[right][0]
                earliest = year
            right += 1

        left+=1
        right = left+1
    return earliest


if __name__=="__main__":
    #logs = [[1952, 1981], [1952, 2003], [1953, 1993], [1968, 1973], [1976, 2032], [1982, 2048], [1983, 1997], [1999, 2021], [2003, 2016], [2010, 2018]]
    logs = [[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]]
    print(maxPopulation(logs))