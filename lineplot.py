# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1.0, 2.0, 3.0, 4.0]
# corresponding y axis values
y = [16.22, 9.090, 25, 29.411]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel("x - axis")
# naming the y axis
plt.ylabel("y - axis")

# giving a title to my graph
plt.title("My first graph!")

# function to show the plot
plt.show()
