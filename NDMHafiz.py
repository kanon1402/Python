import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=10.168.2.164;'
                        # 'SERVER=137.116.139.217;'
                        'DATABASE=ARCHND;'
                        'UID=sa;PWD=erp')

query = """
declare @today varchar(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
declare @previous15days varchar(8) = CONVERT(varchar(8), dateAdd(day,-16,getdate()), 112)
select left(AUDTORG,3) as branchname, SUM(AVG1to15Stock) as Stock 
 from 
(select AUDTORG, cast((sum(QTYONHAND)/15)/1000 as decimal(10,2)) as AVG1to15Stock from ICHistoricalStock
where AUDTDATE between @previous15days and @today and AUDTORG not in ('CENTRAL', 'SKFDAT')
group by AUDTORG) as stockinfo
left join 
(select BRANCH, NDMNAME, LOGINNAME from NDM) as NDM
on left(stockinfo.audtorg,3)=left(NDM.BRANCH,3)
where LOGINNAME='Hafiz'
group by left(AUDTORG,3)
order by branchname

"""

def number_decorator(number):
    number = round(number, 2)
    number = format(number, ',')
    number = number + 'K'
    return number

x = pd.read_sql_query(query, connection)
y = x['branchname'].tolist()
data = x['Stock'].tolist()
# print(data)
data_label = [number_decorator(data[0]), number_decorator(data[1]), number_decorator(data[2]),
        number_decorator(data[3]), number_decorator(data[4]), number_decorator(data[5])]


colors = ['#f9ff00', '#c085e9', '#ff8600', '#5d87a3', '#c1f588', '#e985d6', '#99d3e9']
legend_element = [Patch(facecolor='#f9ff00', label='COX'),
                  Patch(facecolor='#c085e9', label='CTG'),
                  Patch(facecolor='#ff8600', label='CTN'),
                  Patch(facecolor='#5d87a3', label='KUS'),
                  Patch(facecolor='#c1f588', label='NAJ'),
                  Patch(facecolor='#e985d6', label='PBN')
                  ]

fig1, ax = plt.subplots()
pack_all, label, percent_value = ax.pie(data, labels=data_label, colors=colors,
                                        autopct='%.1f%%',
                                        textprops={'color': "Black"}, startangle=90, pctdistance=.70)

plt.setp(percent_value, fontsize=12, color='black', fontweight='bold')
plt.setp(label, fontsize=12)
plt.title('Last 15 days avg stock : Mr. Hafiz', fontsize=18, fontweight='bold', color='#3e0a75')
plt.legend(handles=legend_element, loc='best', fontsize=11)
ax.axis('equal')

plt.tight_layout()
plt.savefig('T3(Hafiz).png')
# plt.show()
