def queens(places,n,i,j):
    k=i+1
    if(k>=n):
        return
    for l in range(n):
        if((k-l)!=(i-j) and (k+l)!=(i+j) and l not in places):
            print(f"i={i}, j={j},k={k},l={l}")
            places.append(l)
            queens(places,n,k,l)
            return
    places.clear()
    return


p=[]
n=8
for i in range(n):
    p.append(i)
    queens(p,n,0,i)
    if p:
        print(p)
        p.clear()
