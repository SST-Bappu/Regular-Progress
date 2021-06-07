from collections import Counter
from copy import deepcopy
class Permutations:
    def permutationsII(self,nums):
        self.nums = nums
        self.cnt = Counter(nums)
        self.arrangement = []
        self.arrange([])
        return self.arrangement
    def arrange(self,cur):
        if len(cur)== len(self.nums):
            self.arrangement.append(cur)
            return
        for key in self.cnt:
            if self.cnt[key]>0:
                new = deepcopy(cur)
                new.append(key)
                self.cnt[key]-=1
                self.arrange(new)
                self.cnt[key]+=1
if __name__=="__main__":
    nums = [1,1,2]
    sol = Permutations()
    print(sol.permutationsII(nums))