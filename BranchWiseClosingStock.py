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
declare @today varchar(8) = CONVERT(varchar(8), dateAdd(day,0,getdate()), 112)
declare @previous15days varchar(8) = CONVERT(varchar(8), dateAdd(day,-15,getdate()), 112)

select left(AUDTORG,3) as AUDTORG, cast((sum(QTYONHAND)/15)/1000 as decimal(10,2)) as AVG1to15Stock from ICHistoricalStock
where AUDTDATE between @previous15days and @today and AUDTORG not in ('CENTRAL', 'SKFDAT')
group by AUDTORG
Order by AVG1to15Stock desc

"""
data = pd.read_sql_query(query, connection)

x = data['AUDTORG'].tolist()
day1_sale = data['AVG1to15Stock'].tolist()


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

bar1 = plt.bar(bar_index, day1_sale, width=.65,
               alpha=opacity, color='#40b7ff', label='Frank')


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + 0.2, height * 1.018,
                number_decorator(height),
                va='bottom',
                fontsize=8, fontweight='bold', rotation=90)


autolabel(bar1)

plt.ylabel('AVG Closing Stock', fontsize=12, fontweight='bold')
plt.xlabel('Branch Name', fontsize=12, fontweight='bold')
plt.title('Branch Item Wise AVG Closing Stock (Last 15 Days)', fontsize=18, fontweight='bold')
plt.xticks(bar_index, x, rotation='vertical')
plt.yticks(np.arange(0, max(day1_sale) + 10, 5))
plt.tight_layout()
plt.savefig('T2.png')
print('Complete')
# plt.show()
