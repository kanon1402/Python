import pandas as pd
import pyodbc as db
import numpy as np
from matplotlib import pyplot as plt

connection = db.connect('DRIVER={SQL Server};'
                        # 'SERVER=10.168.2.164;'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHND;'
                        'UID=sa;PWD=erp@123')

query = """
select left(AUDTORG,3) as branchname, sum(QTYONHAND)/1000 as TodayStock from ICStockStatusCurrent_Lot
where AUDTORG not in ('CENTRAL', 'SKFDAT')
group by AUDTORG
order by sum(QTYONHAND)/1000 DESC

"""
data = pd.read_sql_query(query, connection)

x = data['branchname'].tolist()
day1_sale = data['TodayStock'].tolist()


def number_decorator(number):
    number = round(number, 1)
    number = format(number, ',')
    number = number + 'K'
    return number


def thousand_K_number_decorator(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number


bar_index = np.arange(len(day1_sale))

fig, ax = plt.subplots(figsize=(12, 4.8))

opacity = 1
# colors = ['r', 'g', 'y']
bar1 = plt.bar(bar_index, day1_sale, width=.65,
               alpha=opacity, color='#3ebb91', label='Frank')


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + 0.2, height * 1.01,
                number_decorator(height),
                va='bottom',
                fontsize=8, fontweight='bold', rotation=90)


autolabel(bar1)

plt.ylabel('Current Stock', fontsize=12, fontweight='bold')
plt.xlabel('Branch Name', fontsize=12, fontweight='bold')
plt.title('Branch Item Wise Current Stock', fontsize=18, fontweight='bold')
plt.xticks(bar_index, x, rotation='vertical')
plt.yticks(np.arange(0, max(day1_sale) + 10, 5))

plt.tight_layout()
plt.savefig('T1.png')
print('Complete')
# plt.show()
