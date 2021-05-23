def JumpGame(s,minjump,maxjump):
    return PerformRecur(s,len(s)-1,minjump,maxjump)
def PerformRecur(s,j,minJump,maxJump):
    if s[j] == '1' or j<0:
        return False
    if j==0:
        return True
    return PerformRecur(s,j-minJump,minJump,maxJump) or PerformRecur(s,j-maxJump,minJump,maxJump)

if __name__=="__main__":
    s = "01111111011110"
    print(JumpGame(s,1,9))