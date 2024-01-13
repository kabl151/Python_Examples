from queue import Queue

Q = Queue()
Q.put(1)
Q.put(2)
x = Q.get()

print(x)