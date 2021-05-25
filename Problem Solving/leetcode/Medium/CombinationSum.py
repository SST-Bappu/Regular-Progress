class FindCombinationSum:
    def CombinationSum(self,numb,target):
        self.result = set()
        self.result_Dfs = []
        numb.sort()
        # self.Combination(numb,0,(),target)
        self.DfsCombination(numb,[],target)
        return self.result_Dfs
    def Combination(self,numb,i,select,rem):
        if rem == 0:
            self.result.add(select)
        if rem<0:
            return
        if i>= len(numb):
            return
        self.Combination(numb,i,select+(numb[i],),rem-numb[i])
        self.Combination(numb,i+1,select,rem)

    def DfsCombination(self,numb,select,rem):
        if rem == 0:
            self.result_Dfs.append(select)
            return
        if rem<0:
            return
        for i in range(len(numb)):
            if numb[i]>rem:
                break
            self.DfsCombination(numb[i:],select+[numb[i]],rem-numb[i])

if __name__=="__main__":
    numb = [2,3,6,7]
    sol = FindCombinationSum()
    print(sol.CombinationSum(numb,7))
