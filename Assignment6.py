import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

A = 300
B = 400
C = 700
D = 200
E = 150

data = [A, B, C, D, E]
print(data)

colors = ['#f9ff00', '#ff8600', '#5d87a3', '#e985d6', '#c085e9']
legend_element = [Patch(facecolor='#f9ff00', label='A'),
                  Patch(facecolor='#ff8600', label='B'),
                  Patch(facecolor='#5d87a3', label='C'),
                  Patch(facecolor='#e985d6', label='D'),
                  Patch(facecolor='#c085e9', label='E')
                  ]

fig1, ax = plt.subplots()

pack_all, label, percent_value = ax.pie(data, labels=data, colors=colors,
                                        autopct='%.1f%%',
                                        textprops={
                                            'color': "Black"}, startangle=90, pctdistance=.80)

plt.setp(percent_value, fontsize=14, color='blue', fontweight='bold')
plt.setp(label, fontsize=14, fontweight='bold')
plt.title('Product wise Sales-Kanon', fontsize=14, fontweight='bold', color='#3e0a75')
plt.legend(handles=legend_element, loc='lower left', fontsize=11)
ax.axis('equal')

plt.tight_layout()
plt.savefig('Assignment6.png')
# plt.show()
