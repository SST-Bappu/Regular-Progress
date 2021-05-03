def parens(n):
    arrangements = []
    arrange(n,n,n,arrangements)
    return arrangements
def arrange(n,open,closed,arrangements,s=''):
   if len(s)==2*n:
       arrangements.append(s)
       return

   if open>0:
       arrange(n,open-1,closed,arrangements,s+'(')

   if closed>open:
       arrange(n,open,closed-1,arrangements,s+')')

if __name__=="__main__":
    print(parens(4))