import pandas as pd
import pyodbc as db
import numpy as np
from matplotlib import pyplot as plt

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHND;'
                        'UID=sa;PWD=erp@123')

query = """

declare @todate varchar(8) = 20200831 --CONVERT(varchar(8), dateAdd(day,0,getdate()), 112)
declare @ystdate varchar(8) = 20200830 --CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
declare @date varchar(6) = 202008 --CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)

select RSMNAME, right(transdate, 2) as transdate, YstSales/1000 as YstSales from 
(select RSMTR, transdate, SUM(EXTINVMISC) as YstSales from OESALESDETAILS
where transtype =1 and left(TRANSDATE,6) = @date and TRANSDATE <> @todate and RSMTR is not null and RSMTR <> '0' and RSMTR <> 'ZREGION'
group by RSMTR, transdate) as t1
left join
(select DISTINCT RSMTR, RSMNAME from V_RFieldForce
where YEARMONTH = @date and RSMTR not like '%INS%') as t2
on t1.RSMTR=t2.RSMTR
where RSMNAME is not null
order by RSMNAME ASC, TRANSDATE asc


"""
data = pd.read_sql_query(query, connection)
print(data)
akhterdf = data[data['RSMNAME'] == 'Akhter']
Atikdf = data[data['RSMNAME'] == 'Atik']
Byrondf = data[data['RSMNAME'] == 'Byron']
Koushikdf = data[data['RSMNAME'] == 'Koushik']
Pradipdf = data[data['RSMNAME'] == 'Pradip']
Rubeldf = data[data['RSMNAME'] == 'Rubel']
Shafiqdf = data[data['RSMNAME'] == 'Shafiq']
Shakibdf = data[data['RSMNAME'] == 'Shakib']
Shoheldf = data[data['RSMNAME'] == 'Shohel']

fig, ax = plt.subplots(figsize=(16, 8))

line1 = ax.plot(akhterdf['transdate'].tolist(), akhterdf['YstSales'].tolist(), color='red', marker='o', label='Akhter')
line2 = ax.plot(Atikdf['transdate'].tolist(), Atikdf['YstSales'].tolist(), color='blue', marker='*', label='Atik')
line3 = ax.plot(Byrondf['transdate'].tolist(), Byrondf['YstSales'].tolist(), color='yellow', marker='s', label='Byrond')
line4 = ax.plot(Koushikdf['transdate'].tolist(), Koushikdf['YstSales'].tolist(), color='#d46d57', marker='p', label='Koushik')
line5 = ax.plot(Pradipdf['transdate'].tolist(), Pradipdf['YstSales'].tolist(), color='#88c200', marker='1', label='Pradip')
line6 = ax.plot(Rubeldf['transdate'].tolist(), Rubeldf['YstSales'].tolist(), color='#3c67a8', marker='p', label='Rubel')
line7 = ax.plot(Shafiqdf['transdate'].tolist(), Shafiqdf['YstSales'].tolist(), color='#9da83c', marker='D', label='Shafiq')
line8 = ax.plot(Shakibdf['transdate'].tolist(), Shakibdf['YstSales'].tolist(), color='#47dd07', marker='H', label='Shakib')
line9 = ax.plot(Shoheldf['transdate'].tolist(), Shoheldf['YstSales'].tolist(), color='#a83c8f', marker='v', label='Shohel')


ax.legend(loc='best')
plt.xlabel("Date", color='black', fontsize=14, fontweight='bold')
plt.ylabel("Sales in Thousands", color='black', fontsize=14, fontweight='bold')

plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.title('RSM MTD Sales', fontweight='bold', color='#3e0a75',  fontsize=18)

# for a, b in zip(x, y):
#     plt.text(a, b, str(b) + 'K', ha='center', va='bottom')

# for a, b in zip(x, z):
#     plt.text(a, b, str(b) + 'K', ha='center', va='bottom')

print('complete')
plt.tight_layout()
plt.savefig('rsm_mtd_sales.png')
plt.show()


# # # Area chart ------- using seaborn
# plt.fill_between(akhterdf['transdate'].tolist(), akhterdf['YstSales'].tolist(), color="red", alpha=0.3, label='akhter')
# plt.fill_between(Atikdf['transdate'].tolist(), Atikdf['YstSales'].tolist(), color='green', label='Atik', alpha=.4)
# plt.legend(loc='Best')
# plt.show()