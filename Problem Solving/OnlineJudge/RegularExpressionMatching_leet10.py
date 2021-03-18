def RegularExpressionMatching(list,grammar):
    i = j = 0
    keep = None
    while(i<len(grammar) and j<len(grammar)):
        if grammar[i]=='.' and (i+1)<len(grammar) and grammar[i+1]=='*':
            if (i+2)>=len(grammar):
                return True
            i+=2
            while(j<len(list) and grammar[i]!=list[j]):
                j+=1
        elif i+1<len(grammar) and grammar[i+1]=='*':
            while(j<len(list)) and (grammar[i]==list[j]):
                keep = list[j]
                j+=1
            i+=2
            while(i<len(grammar) and grammar[i]==keep):
                i+=1
        elif grammar[i]=='.':
            j+=1
            i+=1
        elif j<len(list) and grammar[i]!=list[j]:
            return False
        else:
            i+=1
            j+=1
    return True if (j>=len(list) and i>=len(grammar)) else False

if __name__=="__main__":
    str = "aaa"
    grammar = "ab*a*c*a"
    print(RegularExpressionMatching(str,grammar))