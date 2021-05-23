def RotatedArray(arr,target):
    left = 0
    right = len(arr)-1
    if arr[left]==target:
        return left
    if arr[right]==target:
        return right
    if target>arr[left]:
        left+=1
        while left < len(arr) and arr[left]>arr[left-1]:
            if arr[left] == target:
                return left
            left+=1
    elif target<arr[right]:
        right-=1
        while right>=0 and arr[right]<arr[right+1]:
            if arr[right] == target:
                return right
            right-=1
    return -1
if __name__=="__main__":
    arr = [1]
    print(RotatedArray(arr,3))