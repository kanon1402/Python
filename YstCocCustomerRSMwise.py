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

declare @ystdate varchar(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
declare @date varchar(6) = CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)

select RSMNAME, YSTTotalCust from 
(select RSMTR, COUNT(DISTINCT CUSTOMER) as YSTTotalCust from OESALESDETAILS
where TRANSDATE = @ystdate and RSMTR is not null and RSMTR <> '0' and RSMTR <> 'ZREGION'
group by RSMTR) as t1
left join
(select DISTINCT RSMTR, RSMNAME from V_RFieldForce
where YEARMONTH = @date and RSMTR not like '%INS%') as t2
on t1.RSMTR=t2.RSMTR
where RSMNAME is not null
order by YSTTotalCust desc

"""
data = pd.read_sql_query(query, connection)

x = data['RSMNAME'].tolist()
day1_sale = data['YSTTotalCust'].tolist()


def number_decorator(number):
    number = round(number, 1)
    number = format(number, ',')
    number = number
    return number


def thousand_K_number_decorator(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number
    return number


bar_index = np.arange(len(day1_sale))

fig, ax = plt.subplots(figsize=(12, 4.8))

opacity = 1

bar1 = plt.bar(bar_index, day1_sale, width=.65,
               alpha=opacity, color='#40b7ff', label='Frank')


def autolabel(bar1):
    for bar in bar1:
        height = int(bar.get_height())
        ax.text(bar.get_x() + 0.2, height * 1.01,
                number_decorator(height),
                va='bottom',
                fontsize=8, fontweight='bold')


autolabel(bar1)

plt.ylabel('Yesterday Covered Customer', fontsize=12, fontweight='bold')
plt.xlabel('RSM Name', fontsize=12, fontweight='bold')
plt.title('Yesterday Covered Customer RSM Wise', fontsize=18, fontweight='bold')
plt.xticks(bar_index, x)
plt.yticks(np.arange(0, max(day1_sale) + 10, 25))
plt.tight_layout()
# plt.savefig('T2.png')
print('Complete')
plt.show()
