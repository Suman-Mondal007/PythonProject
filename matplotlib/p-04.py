import matplotlib.pyplot as plt

x = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri']
y = [10, 15, 7, 20, 12]

plt.pie(y, labels=x, autopct='%1.1f%%', colors=['red', 'green', 'blue', 'yellow', 'purple'])
plt.title('Book Sales Data')
plt.show()
