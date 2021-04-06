def CourseScheduler(n, PreReq):
    ReqHash={}
    i=0
    while i<len(PreReq):
        if not ReqHash.get(PreReq[i][0]):
            ReqHash[PreReq[i][0]] = []
        j=1
        while j<len(PreReq[i]):
            ReqHash[PreReq[i][0]].append(PreReq[i][j])
            j+=1
        i+=1
    Done={}
    print(ReqHash)
    for key in ReqHash:
        print(key,end=": " )
        for item in ReqHash[key]:
            print(item,end =" ")
        print("")
    '''
    for key in ReqHash:
        if not Done.get(key):
            if not Traverse(key,ReqHash):
                return False
            Done[key] = True'''



def Traverse(key,ReqHash,check={}):
    check[key]=True
    for item in ReqHash[key]:
        if check.get(item):
            return False
        if not Traverse(item,ReqHash,check):
            return False
    return True

if __name__=="__main__":
    PreReq = [[1,0],[2,1],[2,5],[0,3],[4,3],[3,5],[4,5]]
    print(CourseScheduler(6,PreReq))