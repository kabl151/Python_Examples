class CircleQueue:
    N, K = 0, 0
    rear = 0
    front = 0
    MAX_SIZE = 0
    queue = list()
    
    def __init__(self):
        self.rear = 0
        self.front = CircleQueue.K
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
    
    def dequeue_by(self):
        if self.is_empty():
            print("ERROR: EMPTY")
            return
        self.front = ((self.front + 3) % self.MAX_SIZE)
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
lolQue.N, lolQue.K = map(int, input().split())

lolQue.MAX_SIZE = lolQue.N + 1
for i in range(lolQue.N+1):
    lolQue.enqueue(i+1)

while lolQue.is_empty() == False:
    lolQue.dequeue_by()
    
    print(lolQue.queue_print())

# print(lolQue.queue_print())
# print(lolQue.queue)