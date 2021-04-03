adjlist={
    1:[0,1,2],
    2:[3,4,5],
    3:[6,7,8],
}

adjlist[1].remove(0)
for item in adjlist[1]:
    print(item)
print(type(adjlist))