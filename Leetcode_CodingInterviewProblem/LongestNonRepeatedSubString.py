def NonRepeatedSubstring(string):
    hash = dict()
    longestSubString = 0
    left = right =0
    while(right<len(string)):
        if hash.get(string[right]):
            longestSubString = max(longestSubString,right-left-1)
            hash.update({string[right]:right})
            left = right
            right +=1
        else:
            hash.update({string[right]:right})
            right+=1

    longestSubString= max(longestSubString,right-left-1)
    return longestSubString
if __name__=="__main__":
    string = "abcdabcd"
    print(NonRepeatedSubstring(string))
