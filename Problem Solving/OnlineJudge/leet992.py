class Solution:
    def subarraysWithKDistinct(self,arr,k):
        left = 0
        subarr=[][]
        j=0
        slw=k
        while True:
            cnt = 0
            for k in range(i,i+slw):
                if arr[k] not in subarr[j]:
                    cnt += 1
                subarr[j].append(arr[k])