def maxDistance(nums1,nums2):
    maxDist = 0
    left = right = 0
    while right <len(nums2):
        if nums2[right]<nums1[left]:
            maxDist = max(maxDist,(right-1-left))
            left+=1
            if right<left:
                right = left
        else:
            right += 1

    return max(maxDist,(right-1-left))

if __name__=="__main__":
    nums1 = [5,4]
    nums2 = [3,2]
    print(maxDistance(nums1,nums2))