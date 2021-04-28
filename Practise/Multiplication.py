def multiply(m,n):
    small = min(m,n)
    big = max(m,n)
    return Recursion(small,big)
def Recursion(small,big):
    if small == 1:
        return big
    if small == 0:
        return 0
    half = small//2
    result1 = Recursion(half,big)
    result2 = result1
    if small%2!=0:
        result2 = Recursion(small-half,big)
    return result1+result2
if __name__=="__main__":
    print(multiply(5,6))