def MergeIntervals(intervals,insert):
    result = []
    if not len(intervals):
        return [insert]
    chk = False
    if insert[0] <= intervals[0][0]:
        result.append(insert)
        chk = True
    i = 0
    while i < len(intervals):
        n = len(result)
        if n == 0 or (result[n-1][1]<intervals[i][0] and (chk or intervals[i][0]<=insert[0])) :
            result.append(intervals[i])

        elif not chk:
            if result[n-1][1]<insert[0]:
                result.append(insert)
            else:
                result[n-1][1] = max(result[n-1][1],insert[1])
                result[n-1][0] = min(result[n-1][0],insert[0])
            chk = True
            i-=1
        else:
            result[n-1][1] = max(result[n-1][1],intervals[i][1])
            result[n-1][0] = min(result[n-1][0],intervals[i][0])
        i+=1
    if not chk:
        n = len(result)
        if result[n-1][1]<insert[0]:
            result.append(insert)
        else:
            result[n - 1][1] = max(result[n - 1][1], insert[1])
            result[n - 1][0] = min(result[n - 1][0], insert[0])
    return result
if __name__=="__main__":
    intervals = [[1,5]]
    insert = [0,0]
    print(MergeIntervals(intervals,insert))