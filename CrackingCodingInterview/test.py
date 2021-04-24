class box:
    def __init__(self,height,width,depth):
        self.height = height
        self.width = width
        self.depth = depth
    def __lt__(self, other):
        return self.height<other.height
    def __eq__(self, other):
        return self.height == other.height

if __name__=="__main__":
    boxes = [box(3,2,1),box(6,5,4)]
    print(boxes[0].height, boxes[0].width, boxes[0].depth)
    print(boxes[1].height, boxes[1].width, boxes[1].depth)
    boxes.sort(reverse=True)
    print(boxes[0].height, boxes[0].width, boxes[0].depth)
    print(boxes[1].height, boxes[1].width, boxes[1].depth)
    new = enumerate(boxes)
    print(list(new))