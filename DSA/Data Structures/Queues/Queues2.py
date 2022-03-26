
# Queues
import random
print("Implementing Queue First IN First OUT")
que = []
print("Queue:", que)
i=1
while len(que) < 4:
    n = random.randint(0, 20)
    que.append(n)
    print("Queue: After First IN:", i, "iteration", que)
    i = i+1
j = 1
while len(que) > 0:
    que.pop(0)
    print("Queue: After First OUT:", j, "iteration", que)
    j = j + 1

