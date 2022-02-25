import queue

my_Q = queue.Queue(3)

my_Q.put(1)
my_Q.put(2)
my_Q.put(3)

print(my_Q.qsize())