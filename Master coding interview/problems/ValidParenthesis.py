def ValidParenthesis(paren):
    last = -1
    stack=[]
    for c in range(len(paren)):
        if (str[c]=='}' or str[c]==']' or str[c]==')') and last>=0:
            if str[c]=='}' and stack[last]!='{':
                return False
            elif str[c] == ']' and stack[last] != '[':
                return False
            elif str[c] == ')' and stack[last] != '(':
                return False
            else:
                stack.pop()
                last-=1
        else:
            stack.append(paren[c])
            last+=1
    return True if len(stack)==0 else False
def Solution2(str):
    last = -1
    n= len(str)
    c=0
    str=list(str)
    while(c<n):
        if (str[c]=='}' or str[c]==']' or str[c]==')') and last>=0:
            if str[c]=='}' and str[last]!='{':
                return False
            elif str[c] == ']' and str[last] != '[':
                return False
            elif str[c] == ')' and str[last] != '(':
                return False
            else:
                str.pop(c)
                str.pop(last)
                last-=1
                n-=2
                c-=2
        else:
            last+=1
        c+=1
    return len(str)==0

if __name__=="__main__":
    str = "()[]{"
    print(ValidParenthesis(str))

