class permutations:
    def permut(self,nums):
        self.nums = nums
        self.arrangements = []
    def arrange(self,i,cur=[]):
        if len(cur) == len(self.nums):
            self.arrangements.append(cur)
            return
        
