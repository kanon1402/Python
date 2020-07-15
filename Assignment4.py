import pandas as pd
import pyodbc as db
import numpy as np
from matplotlib import pyplot as plt

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=10.168.2.164;'
                        'DATABASE=ARCHND;'
                        'UID=sa;PWD=erp')

query = """

DECLARE @ThisMonth CHAR(6) = CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)
DECLARE @lastmnth CHAR(6) = CONVERT(varchar(6), dateAdd(MONTH,-1,getdate()), 112)

select top 10 AUDTORG, 
cast(SUM(case when LEFT(TRANSDATE,6) = @ThisMonth then EXTINVMISC END)/1000000 as  decimal(10,2)) as ThisMonthSales,
cast(SUM(case when LEFT(TRANSDATE,6) = @lastmnth then EXTINVMISC END)/1000000 as  decimal(10,2)) as LastMonthSales
from OESalesDetails
group by AUDTORG"""
data = pd.read_sql_query(query, connection)

x = data['AUDTORG'].tolist()
y = data['ThisMonthSales'].tolist()
z = data['LastMonthSales'].tolist()
# print(x)
# print(y)
# print(z)
fig, ax = plt.subplots()

ax.plot(x, y, color='red', marker='o')
ax.plot(x, z, color='blue', marker='o')
ax.legend(labels=('This Month', 'Last Month'), loc='best')
plt.xlabel("Branch Name", color='black', fontsize=14, fontweight='bold')

plt.ylabel("Sales", color='black', fontsize=14, fontweight='bold')
plt.yticks(np.arange(0, 21, 5))
plt.title('Line chart', fontweight='bold', color='#3e0a75',  fontsize=18)

for a, b in zip(x, y):
    plt.text(a, b, str(b) + 'K', ha='center', va='bottom')

for a, b in zip(x, z):
    plt.text(a, b, str(b) + 'K', ha='center', va='bottom')

print('complete')
plt.tight_layout()
# plt.savefig('task.png')
plt.show()
