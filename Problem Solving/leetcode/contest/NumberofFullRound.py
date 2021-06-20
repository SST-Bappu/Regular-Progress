def NumberFullRoound(startTime, finishTime):
    startTime = startTime.strip().split(':')
    finishTime = finishTime.strip().split(':')
    startTime[0] = int(startTime[0])
    startTime[1] = int(startTime[1])
    finishTime[0] = int(finishTime[0])
    finishTime[1] = int (finishTime[1])
    if finishTime[0]==0 and finishTime[0]!=startTime[0]:
        finishTime[0] = 24
    if startTime[1]%15 != 0:
        startTime[1] = (startTime[1]//15)*15+15
    if finishTime[1]%15 != 0:
        finishTime[1] = (finishTime[1]//15)*15
    result = 0

    if startTime[0] == finishTime[0]:
        if startTime[1]>=finishTime[1]:
            result+=24*4 - (startTime[1]-finishTime[1])//15
        else:
            result+=(finishTime[1]-startTime[1])//15
        return result
    if startTime[0]>finishTime[0]:
        result += (24-startTime[0]+finishTime[0])*4
    else:
        result+= (finishTime[0] - startTime[0])*4
    if startTime[1]>finishTime[1]:
        result -= (startTime[1]-finishTime[1])//15
    elif finishTime[1]>startTime[1]:
        result+=(finishTime[1]-startTime[1])//15
    return result

if __name__=="__main__":
    print(NumberFullRoound("00:40","00:05"))
