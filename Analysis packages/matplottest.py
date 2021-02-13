# import matplotlib
# matplotlib.use('Agg')  # no UI backed
import matplotlib.pyplot as plt    # Import pyplot as a convention
import numpy as np
plt.plot([2.3, 3.6, 7.8], [4.2, 1.7, 7.4])    # Plot some co-ordinates
plt.show()
# plt.savefig('testfig.png') # Saves the figure in an image


# Legends, Labels, Colors etc
# Line 1
X1 = ([2, 4, 6, 10])
Y1 = ([4, 6, 6, 8])

# Line 2
X2 = ([2, 4, 6, 10])
Y2 = ([2, 4, 8, 10])

# Plotting, linestyle, color and legends
plt.plot(X1, Y1, linestyle = '--', c = 'g', label = 'Line 1')
plt.plot(X2, Y2, linestyle = '--', c = 'r', label = 'Line 2')
plt.legend()

plt.title('Matplotlib Demo') # Set title

# Set labels
plt.xlabel('X - Value')
plt.ylabel('Y - Value')

# Set axis ticks
plt.xticks([0, 2, 4, 6, 8, 10, 12])
plt.yticks([0, 2, 4, 6, 8, 10, 12])

plt.show()

plt.savefig('plots.png')

# Bar plots and Histograms
# Bar plots
plt.bar([11, 14, 19, 13, 16], [0.2, 0.4, 0.6, 0.8, 1.0])
plt.xticks(np.arange(11, 20))
plt.title('Bar Graph Example')
plt.show()

# Histogram
IQ = [85, 92, 115, 121, 72, 102, 104, 99, 110, 120, 121, 122, 90, 115, 119, 92, 98, 110, 138]
Age = [70, 80, 90, 100, 110, 120, 130, 140, 150]

plt.hist(IQ, Age, histtype='bar', rwidth=0.8)
plt.xlabel('IQ range')
plt.ylabel('No. of Students')

plt.title('Histogram Example')
plt.legend()

plt.show()

# Scatter Plots
# Get some random points
x = np.random.randn(200)
y = np.random.randn(200)

plt.scatter(x, y, c='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Example')

plt.show()

# Pie Chart
Programming_Languages = ["c", "C++", "Java", "Python", "ruby", "php"]
Usage = [10, 20, 40, 60, 20, 30]

# Pie chart is oval by default
# To make it a circle
plt.axis('equal')

plt.pie(Usage, labels=Programming_Languages, shadow=True)
plt.title("Pie Chart Example")
plt.show()