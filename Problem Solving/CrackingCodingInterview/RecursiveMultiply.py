def RecursiveMultiply(n,m):
    if m==0:
        return 0
    return n+RecursiveMultiply(n,m-1)
if __name__=="__main__":
    print(RecursiveMultiply(5,3))