from collections import deque
class LRU:
    cache=deque()
    hash = {}
    def __init__(self,capacity):
        self.capacity = capacity
    def get(self,key):
        if not self.hash.get(key):
            return -1
        else:
            value = self.hash[key]-1
            self.cache.remove(key)
            self.cache.append(key)
            return value
    def put(self,key,value):
        if not self.hash.get(key):
            if len(self.cache) == self.capacity:
                oldest = self.cache.popleft()
                self.hash.pop(oldest)
        else:
            self.cache.remove(key)
        self.hash[key] = value+1
        self.cache.append(key)
if __name__=="__main__":
    lru  = LRU(2)
    lru.put(1,0)
    lru.put(2,2)
    lru.put(3,3)
    lru.put(4,4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
