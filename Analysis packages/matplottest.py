# import matplotlib
# matplotlib.use('Agg')  # no UI backed
import matplotlib.pyplot as plt    # Import pyplot as a convention

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