def LargestOdd(num):
    n = len(num)
    if not n:
        return ""
    for i in reversed(range(n)):
        if int(num[i])%2 != 0:
            return num[:i+1]
    return ""
if __name__=="__main__":
    print(LargestOdd('35438'))
