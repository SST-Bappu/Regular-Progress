def BoatsToSave(people,limit):
    i=Boats = 0
    j = len(people)-1
    people.sort()
    while(i<=j):
        if i!=j:
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            else:
                j-=1
        else:
            i+=1
        Boats+=1
    return Boats
if __name__=="__main__":
    people = [3,2,3,1,2]
    print(BoatsToSave(people,3))