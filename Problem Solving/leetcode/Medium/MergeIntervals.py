def MergeIntervals(intervals):
    intervals.sort()
    result = []
    for interval in intervals:
        n = len(result)
        if n == 0 or result[n-1][1]<interval[0] :
            result.append(interval)
        else:
            result[n-1][1] = max(result[n-1][1],interval[1])
            result[n-1][0] = min(result[n-1][0],interval[0])
    return result
if __name__=="__main__":
    intervals = [[1,4],[0,0]]
    print(MergeIntervals(intervals))