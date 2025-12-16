# import matplotlib.pyplot as plt
#
# # Data for three groups
# weight_g1 = [55, 57, 60, 62, 65]
# height_g1 = [112, 125, 98, 145, 152]
#
# weight_g2 = [58, 61, 63, 64, 66]
# height_g2 = [195, 155, 180, 122, 132]
#
# weight_g3 = [68, 70, 71, 72, 69]
# height_g3 = [160, 175, 170, 130, 230]
#
# # Scatter plot
# plt.scatter(weight_g1, height_g1, marker='*', label='Group 1')
# plt.scatter(weight_g2, height_g2, marker='o', label='Group 2')
# plt.scatter(weight_g3, height_g3, marker='^', label='Group 3')
#
# # Labels and title
# plt.xlabel("Weight")
# plt.ylabel("Height")
# plt.title("Group wise Weight vs Height scatter plot")
# plt.legend()
#
# plt.show()


import matplotlib.pyplot as plt

# Data for lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# Plot two lines
plt.plot(x, y1, marker="^" ,label='Line 1')
plt.plot(x, y2, label='Line 2')

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Line Plot")
plt.legend()

plt.show()
