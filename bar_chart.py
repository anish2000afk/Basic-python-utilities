import matplotlib.pyplot as plt

# x-coordinates of left sides of bars 
left = [1.0, 2.0, 3.0, 4.0]

# heights of bars
height = [16.22,9.090,25,29.411]
# labels for bars
tick_label = ['Advance accounts', 'Law', 'DT', 'IDT']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('Subjects')
# naming the y-axis
plt.ylabel('Progress')
# plot title
plt.title('20/1/2025')

# function to show the plot
plt.show()
