import math
class Permutations:
    def PermutationSequence(self,n,k):
        nums = [i for i in range(1,n+1)]
        permutation = ""
        k-=1
        while n>0:
            n-=1
            i, k = divmod(k,math.factorial(n))
            permutation+=str(nums[i])
            nums.pop(i)
        return permutation
if __name__=="__main__":
    sol = Permutations()
    print(sol.PermutationSequence(4,4))