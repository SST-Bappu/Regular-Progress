class FindCombination:
    def CombinationSum(self,numb,target):
        self.result = set()
        numb.sort()
        self.Comibination(numb,(),target)
        # self.Combination_backtrack(0,numb,(),target)
        return self.result
    def Comibination(self,numb,select,rem):
        if rem == 0:
            self.result.add(select)
        if rem<0:
            return
        for i in range(len(numb)):
            if i>0 and numb[i]==numb[i-1]:
                continue
            self.Comibination(numb[i+1:],select+(numb[i],),rem-numb[i])
    def Combination_backtrack(self,i,numb,select,rem):
        if rem==0:
            self.result.add(select)
        if rem<0:
            return
        if i>= len(numb):
            return
        self.Combination_backtrack(i+1,numb,select+(numb[i],),rem-numb[i])
        self.Combination_backtrack(i+1,numb,select,rem)

if __name__=="__main__":
    numb = [10,1,2,7,6,1,5]
    sol = FindCombination()
    print(sol.CombinationSum(numb,8))