import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def convert(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number


A = 3000
B = 4000

data = [A, B]
total = data[0] + data[1]
total = 'Total \n' + str(convert(total))
print(data)
print(total)

colors = ['#f9ff00', '#ff8600', '#5d87a3', '#e985d6', '#c085e9']
legend_element = [Patch(facecolor='#f9ff00', label='A'),
                  Patch(facecolor='#ff8600', label='B')
                  ]

A = convert(data[0])
B = convert(data[1])
Data_label = [A, B]

fig, ax = plt.subplots()
pack_all, label, percent_value = ax.pie(data, labels=Data_label, colors=colors,
                                        autopct='%.1f%%',
                                        textprops={
                                            'color': "Black"}, startangle=90, pctdistance=.80)

plt.setp(percent_value, fontsize=14, color='blue', fontweight='bold')
plt.setp(label, fontsize=14, fontweight='bold')

ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold')
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('Product wise Sales', fontsize=14, fontweight='bold', color='#3e0a75')
ax.axis('equal')
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
plt.tight_layout()
# plt.savefig('Donut_Chart.png')
plt.show()
