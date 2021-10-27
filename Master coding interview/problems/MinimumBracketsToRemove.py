import timeit
def MinimumBrackets(str):
    str = list(str)
    leftParen = 0
    i=0
    HashTable = dict()
    chk = False
    while(i<len(str)):
        if str[i]==')' and leftParen<=0:
            str[i]=" "
        elif str[i] == ')' and not chk:
            str[i]=" "
            str[HashTable.get(leftParen)]=" "
            leftParen-=1
        elif str[i]==')':
            leftParen-=1
        elif str[i]=='(':
            leftParen += 1
            HashTable.update({leftParen:i})
            chk = False
        elif str[i]!=" ":

            chk = True
        i+=1
    while(leftParen>0):
        str[HashTable.get(leftParen)]=" "
        leftParen-=1
    return "".join(str)
def RemoveMinimunParenthesis(str): #Solution using Stack
    str = list(str)
    stack=[]
    for i in range(len(str)):
        if str[i]=='(':
            stack.append(i)
        elif str[i]==')' and len(stack):
            stack.pop()
        elif str[i]==')':
            str[i]=''
    while len(stack):
        index = stack.pop()
        str[index] = ''
    return ''.join(str)
if __name__=="__main__":
    str = "(ab(c)d)"
    t1 = timeit.default_timer()
    str = RemoveMinimunParenthesis(str)
    print(str)
    print(timeit.default_timer()-t1)
