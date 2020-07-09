from matplotlib import pyplot as plt

# x = ['A', 'B', 'C', 'D', 'E']
# y = [24, 40, 30, 50, 45]
#
# plt.plot(x, y, color = 'red')
#
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.title('Line chart')
# plt.show()

# # For multiple lines ---------------------
x = ['A', 'B', 'C', 'D', 'E']
y = [24, 40, 25, 50, 45]
z = [10, 20, 28, 14, 35]

# # left, right, weight, hight (0,0,1,1)-----
fig, ax = plt.subplots()
ax.plot(x, y, color='red')
ax.plot(x, z, color='blue')

ax.legend(labels=('Math', 'English'), loc='best')  # legend placed at lower right
plt.xlabel("Name",  color='black', fontsize=14, fontweight='bold')
plt.ylabel("Marks", color='black', fontsize=14, fontweight='bold')
plt.title('Line chart', fontweight='bold', color='#3e0a75',  fontsize=18)
plt.show()
plt.tight_layout()
# plt.savefig('linechart.png')