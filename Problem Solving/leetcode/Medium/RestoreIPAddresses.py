def RestoreIPAddresses(nums):
    address = []
    FindAddress(address,0,"",nums)
    return address

def FindAddress(address,i,cur,nums):
    if i==4:
        address.append(cur)
        return
    if not nums:
        return
    if i ==3:
        if len(nums)>1 and nums[0]=='0':
            return
        if int(nums)<=255:
            FindAddress(address,i+1,cur+nums,"")
        else:
            return
    if i<3:
        for j in range(1,3):
            if j==2 and int(nums[:j])<10:
                continue
            FindAddress(address,i+1,cur+nums[:j]+'.',nums[j:])
        key = nums[:3]
        if int(key)>=100 and int(key)<=255:
            FindAddress(address,i+1,cur+key+'.',nums[3:])

if __name__=="__main__":
    nums = "101023"
    print(RestoreIPAddresses(nums))