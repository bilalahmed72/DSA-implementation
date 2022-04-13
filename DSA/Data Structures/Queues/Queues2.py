
# Queues
# Another Approach
import random
print("Implementing Queue First IN First OUT with another approach: ")
que2 = []
print("Queue:", que2)
i=1
while len(que2) < 4:
    n = random.randint(0, 20)
    que2.append(n)
    print("Queue: After First IN:", i, "iteration", que2)
    i = i+1
j = 1
while len(que2) > 0:
    que2.pop(0)
    print("Queue: After First OUT:", j, "iteration", que2)
    j = j + 1

print("This is Queue Implemented..")    

