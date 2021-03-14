class solution:
    def target_index(self,target,x):
        for i in range(len(x)):
            for j in range(i,len(x)):
                if x[j]==target-x[i]:
                    result=[i,j]
                    return result
        return None
    def target_index_optimized(self,target,x):
        self.hashtable=dict()
        for i in range(len(x)):
            if self.hashtable.get(x[i]) is None:
                self.hashtable.update({(target-x[i]): i})
            else:
                return (self.hashtable.get(x[i]), i)
        return None


if __name__=="__main__":
    x = [1, 7, 3, 5, 9, 2]
    twoSum = solution()
    while(twosum.person()):
    result=twoSum.target_index_optimized(11,x)
    print(result)