def letterCombinations(digits):
    map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    arrangements = []
    arrange(map,arrangements,'',digits)
    return arrangements
def arrange(map,arrangements,s,digits,cnt=0):
    if len(s)==len(digits):
        if len(s):
            arrangements.append(s)
        return
    for c in map[digits[cnt]]:
        arrange(map,arrangements,s+c,digits,cnt+1)
if __name__=="__main__":
    print(letterCombinations('234'))