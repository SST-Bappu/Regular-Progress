class permutations:
    def arrange(self,nums):
        combinations = []
        if len(nums) == 0:
            combinations.append([])
            return combinations
        left = nums[0]
        rest = nums[1:]
        combs = self.arrange(rest)
        for comb in combs:
            n = self.insert_numb([left],0,comb)
            combinations.append(n)
            i=1
            for _ in comb:
                n = self.insert_numb([left],i,comb)
                combinations.append(n)
                i+=1
        return combinations
    def insert_numb(self,num,i,comb):
        left = comb[:i]
        right = comb[i:]
        return left+num+right

if __name__=="__main__":
    numb = [1,2,3,4]
    sol = permutations()
    result = sol.arrange(numb)
    print(len(result))



        
