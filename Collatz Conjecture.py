import matplotlib.pyplot as plt

print("This conjecture holds only for natural numbers (i.e. positive integers 1, 2, 3,...).\n")

a = int(input("ENTER LOWER LIMIT: "))
u = int(input("ENTER UPPER LIMIT: "))
iterations = []
values = []

while a == u:
    print("\nUpper Limit can't be same as Lower Limit of range.\n")
    a = int(input("ENTER LOWER LIMIT: "))
    u = int(input("ENTER UPPER LIMIT: "))
    
    
while a < 0 or u < 0:
    print("\nInvalid Entry. This conjecture holds only for natural numbers (i.e. positive integers 1, 2, 3,...).\nEnter Positive Limits for range\n")
    a = int(input("ENTER LOWER LIMIT: "))
    u = int(input("ENTER UPPER LIMIT: "))

while u < a:
    print("\nInvalid Entry. Lower Limit of the can't be greater than the Upper Limit of range. \nDid you mean, Lower limit = " + str(u) + " & Upper Limit = " + str(a) + " (range: " + str(u) + " to " + str(a) + ")" + " ?\n")
    a = int(input("ENTER LOWER LIMIT: "))
    u = int(input("ENTER UPPER LIMIT: "))
    
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

max_iterations = max(iterations)
max_value = values[iterations.index(max_iterations)]
min_iterations = min(iterations)
min_value = values[iterations.index(min_iterations)]

print("\n" + str(min_value) + " has the lowest no. of iterations, " + str(min_iterations) + " in this range.")
print("\n" + str(max_value) + " has the highest no. of iterations, " + str(max_iterations) + " in this range.")

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
