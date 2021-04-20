def parens(n):
    result=[]
    count_parens(n,n,n,result,"")
    return result

def count_parens(n,openParens, closedParens,result,s):
    if len(s)==2*n:
        result.append(s)
    if openParens>0:
        count_parens(n,openParens-1,closedParens,result,s+"(")
    if closedParens>openParens:
        count_parens(n,openParens,closedParens-1,result,s+")")

if __name__=="__main__":
    print(parens(3))