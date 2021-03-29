class LRU:
    def __init__(self,capacity):
        self.capacity = capacity
    def get(self,key):
        if not self.hash.get(key):
            return -1
        else:
            return self.hash[key]
    def put(self,key,value):
