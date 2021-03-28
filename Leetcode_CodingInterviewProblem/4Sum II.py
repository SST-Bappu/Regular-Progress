from collections import defaultdict,Counter
def FourSum(A,B,C,D):
    hash =defaultdict(int)
    for i in range(len(A)):
        for j in range(len(B)):
           key = 0 - (A[i]+B[j])
           hash[key]+=1
    count = 0
    for i in range(len(C)):
        for j in range(len(D)):
            key = C[i]+D[j]
            count+=hash[key]
    print(hash)
    return count
def FourSum_optimal(A,B,C,D):
    AB = Counter([(a+b) for a in A for b in B])
    print(AB)
    return sum([AB[-c-d] for c in C for d in D])
if __name__=="__main__":
    A = [-1,-1]
    B = [-1,1]
    C = [-1,1]
    D = [1,-1]
    print(FourSum_optimal(A,B,C,D))
    print(FourSum(A,B,C,D))