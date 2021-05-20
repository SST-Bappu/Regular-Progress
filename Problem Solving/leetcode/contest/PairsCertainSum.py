class pair:
    def FindSumPairs(self,nums1,nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    def add(self,index,val):
        self.nums2[index]+=val
    def count(self,tot):
        res = 0
        hash={}
        for i in range(len(self.nums1)):
            hash[tot-self.nums1[i]] = hash[tot-self.nums1[i]]+1 if hash.get(tot-self.nums1[i]) else 1
        for j in range(len(self.nums2)):
            if hash.get(self.nums2[j]):
                res+=hash[self.nums2[j]]
        return res
if __name__=="__main__":
    nums1 = [1, 1, 2, 2, 2, 3]
    nums2 = [1, 4, 5, 2, 5, 4]
    result = pair()
    result.FindSumPairs(nums1,nums2)
    result.add(3,2)
    print(result.count(4))