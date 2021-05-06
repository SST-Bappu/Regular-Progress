def generateParenthesis(n):
    arrangements = []
    arrange(n,n,n,arrangements)
    return arrangements
def arrange(n,left,right,arrangements,s=''):
    if len(s)==2*n:
        arrangements.append(s)
        return
    if left>0:
        arrange(n,left-1,right,arrangements,s+'(')
    if right>left:
        arrange(n,left,right-1,arrangements,s+')')

if __name__=="__main__":
    print(generateParenthesis(1))