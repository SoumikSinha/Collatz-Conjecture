import logging as log
import random
import matplotlib.pyplot as plt

a = int(input("ENTER LOWER LIMIT: "))
u = int(input("ENTER UPPER LIMIT: "))
iterations = []
values = []

log.basicConfig(filename = "logs" , level = log.INFO)

while a < u:
    a = a + 1
    n = a 
    i = 0
    print(n)
    
    if n % 2 != 0:
        n = 3*n  + 1
        i = i + 1
        print(int(n))
        while n % 2 == 0:
            n = n / 2
            i = i + 1
            print(int(n))
            if n == 1:
                break
            if n % 2 != 0:
                n = 3*n + 1
                i = i + 1
                print(int(n))
    
    if n % 2 == 0:
        while n % 2 == 0:
            n = n / 2
            i = i + 1
            print(int(n))
            if n == 1:
                break
            if n % 2 != 0:
                n = 3*n + 1
                i = i +1
                print(int(n))
    
    print("No. of iterations is: " + str(i))
    iterations.append(i)
    values.append(a)

    # x axis values
    x = values
    # corresponding y axis values
    y = iterations
      
# plotting the points 
plt.plot(x, y)
      
# naming the x axis
plt.xlabel("Numbers")
# naming the y axis
plt.ylabel("Iterations")
      
# giving a title to my graph
plt.title("Collatz Conjecture")
      
# function to show the plot
plt.show()

log.info(iterations)
log.info(values)
