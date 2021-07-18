def maxNum(text,brokenLetters):
    lst = text.split()
    cnt = len(lst)
    for word in lst:
        for c in brokenLetters:
            if c in word:
                cnt-=1
                break
    return cnt

if __name__=="__main__":
    text = "leet code"
    bk = "e"
    print(maxNum(text,bk))