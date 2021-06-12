from collections import Counter
class Permutations:
    def permutationsII(self,n,k):
        self.limit = k
        self.nums = [i for i in range(1,n+1)]
        self.cnt = Counter(self.nums)
        self.arrangement = []
        self.arrange('')
        return self.arrangement
    def arrange(self,cur):
        if len(cur)== len(self.nums):
            self.arrangement.append(cur)
            return
        for key in self.cnt:
            if self.cnt[key]>0:
                new = cur
                new+=str(key)
                self.cnt[key]-=1
                self.arrange(new)
                if len(self.arrangement)>=self.limit:
                    return
                self.cnt[key]+=1
if __name__=="__main__":
    sol = Permutations()
    print(sol.permutationsII(4,2))