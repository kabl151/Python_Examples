class CircleQueue:
    
    rear = 0
    front = 0
    MAX_SIZE = 8
    queue = list()
    
    def __init__(self):
        self.rear = 0
        self.front = 0
        self.queue = [0 for i in range(self.MAX_SIZE)]
        
    def is_empty(self):
        if self.rear == self.front:
            return True
        return False
    
    def is_full(self):
        if(self.rear+1)%self.MAX_SIZE == self.front:
            return True
        return False
    
    def enqueue(self, x):
        if self.is_full():
            print("ERROR: FULL")
            return
        self.rear = (self.rear+1)%(self.MAX_SIZE)
        self.queue[self.rear] = x
        
    def dequeue(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        self.front = (self.front + 1) % self.MAX_SIZE
        return self.queue[self.front]
    
    def dequeue_by_3(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        self.front = (self.front + 2) % self.MAX_SIZE
        return self.queue[self.front]
    
    def queue_print(self):
        i = self.front
        if self.is_empty():
            print("EMPTY QUEUE")
            return
        while True:
            i = (i+1) % self.MAX_SIZE
            print(self.queue[i], '')
            if i == self.rear:
                break
            
            

lolQue = CircleQueue()
N, K = map(int, input().split())
lolQue.MAX_SIZE = N+1
for i in range(N+1):
    lolQue.enqueue(i+1)

# lolQue.dequeue_by_3()

print(lolQue.queue_print())
print(lolQue.queue)