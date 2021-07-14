def MergeSorted(nums1,nums2,m,n):
    if not n:
        return
    i = j = 0
    while i<m:
        if nums1[i]>nums2[j]:
            tmp = nums1[i]
            nums1[i] = nums2[j]
            nums2[j] = tmp
            nums2.sort()
        i+=1

    while i <(m+n):
        nums1[i] = nums2[j]
        i+=1
        j+=1
if __name__=="__main__":
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    MergeSorted(nums1,nums2,3,3)
    print(nums1)