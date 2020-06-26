class Queue:
    def __init__(self):
        self.entries=[]
        self.size=0
        self.first=0

    def __str__(self):
        printed="< "+ str(self.entries)[1:-1] +">"
        return printed

    def put(self,item):
        self.entries.append(item)
        self.size+=1

    def get(self):
        dequeued=self.entries[self.first]
        self.size -= 1
        self.entries=self.entries[1:]
        return dequeued

    def head(self):
        return self.entries[0]

    def lenght(self):
        if self.first is None:
            raise Exception("空")
        else:
           return self.size



if __name__ == '__main__':
    queue=Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    print(queue)
    print(queue.get())
    print(queue)
    print(queue.head())
