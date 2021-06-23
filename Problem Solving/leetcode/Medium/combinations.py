def combinations(n,k):
    nums = [i for i in range(1,n+1)]
    result = []
    DFS(nums,k,[],result)
    return result
def DFS(nums,k,path,result):
    if len(path) == k:
        result.append(path)
        return
    for i in range(len(nums)):
        DFS(nums[i+1:],k,path+[nums[i]],result)
if __name__=="__main__":
    print(combinations(4,3))