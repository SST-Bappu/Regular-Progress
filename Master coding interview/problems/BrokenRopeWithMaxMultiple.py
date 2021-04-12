def MaxMultiple(n):
    if n//2<2:
        return n
    left = n//2
    right = n-left
    return MaxMultiple(left)*MaxMultiple(right)
if __name__=="__main__":
    print(MaxMultiple(11))