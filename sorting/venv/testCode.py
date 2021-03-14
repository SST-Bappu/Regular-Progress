def swap(a,b):
    if a>b:
        tmp = a
        a=b
        b=tmp

if __name__=="__main__":
    list = [10,2]
    print(list)
    list[0], list[1] = list[1],list[0]
    #swap(list[0],list[1])
    print(list)
