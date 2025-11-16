import matplotlib.pyplot as plt
scores=[1,2,3,4,5,6,7,8,9,10,5,1,2,2,4,4,7,5,8,4,2,3,6]
plt.hist(scores, bins=10, color='purple', edgecolor='black')
plt.xlabel('Scores')
plt.ylabel('Count')
plt.title('score of students')
plt.show()