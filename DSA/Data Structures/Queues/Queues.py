
# Queues
import random
print("Implementing Queue First IN First OUT")
que = []
print("Queue:", que)
i=1
while len(que) < 4:
    n = random.randint(0, 20)
    que.insert(0, n)
    print("Queue: After First IN:", i, "iteration", que)
    i = i+1
j = 1
while len(que) > 0:
    que.pop()
    print("Queue: After First OUT:", j, "iteration", que)
    j = j + 1
print("This is Queue")
