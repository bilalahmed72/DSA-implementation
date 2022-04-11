
#Stacks
import random
print("Demonstration of Stack using LIFO, Last In First Out ")
arr = []
print("Array:",arr)
j = 1
while len(arr) < 5:
    n = random.randint(0, 20)
    arr.append(n)
    print("Array Last IN: After", j, "iteration", arr)
    j = j+1
i = 1
while len(arr) > 0:
    arr.pop()
    print("Array First OUT: After", i, "iteration", arr)
    i=i+1
    
print("Stack Completed and Implemented")
