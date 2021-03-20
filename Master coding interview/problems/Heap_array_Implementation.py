class Heap:
    def __init__(self):
        self.list=[]
def Heap_insertion(Heap, data):
    Heap.list.append(data)
    c = len(Heap.list)-1
    p = (c-1)//2
    while(p>=0 and Heap.list[c]<Heap.list[p]):
        Heap.list[p],Heap.list[c] = Heap.list[c],Heap.list[p]
        c = p
        p = (c-1)//2
def Heap_Deletion(Heap):
    if len(Heap.list)<=1:
        Heap.list.pop()
        return
    Heap.list[0]=Heap.list.pop()
    ReArrange(Heap,0)
def ReArrange(Heap,i):
    if len(Heap.list)<=(2*i+1):
        return
    if (len(Heap.list)==(2*i+2) or Heap.list[2*i+1]<Heap.list[2*i+2]):
        if (Heap.list[i]>Heap.list[2*i+1]):
            Heap.list[i], Heap.list[2 * i + 1] = Heap.list[2 * i + 1], Heap.list[i]
            return ReArrange(Heap, 2 * i + 1)
    elif Heap.list[i]>Heap.list[2*i+2]:
        Heap.list[i], Heap.list[2 * i + 2] = Heap.list[2 * i + 2], Heap.list[i]
        return ReArrange(Heap, 2 * i + 2)

if __name__=="__main__":
    list = [10, 30, 20, 35, 40, 32, 25, 5, 2, 8, 12, 4]
    heap = Heap()
    for item in list:
        Heap_insertion(heap,item)
    print(heap.list)
    Heap_insertion(heap,1)
    print(heap.list)
    Heap_Deletion(heap)
    print(heap.list)
