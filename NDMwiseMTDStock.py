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

declare @today varchar(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
declare @firstdate varchar(8) = CONVERT(varchar(8), DATEADD(MONTH, DATEDIFF(MONTH, 0, GETDATE()), 0), 112)
select LOGINNAME, SUM(MTDAVGStock) as Stock 
 from 
(select AUDTORG, cast((sum(QTYONHAND)/15)/1000 as decimal(10,2)) as MTDAVGStock from ICHistoricalStock
where AUDTDATE between @firstdate and @today and AUDTORG not in ('CENTRAL', 'SKFDAT')
group by AUDTORG) as stockinfo
left join 
(select BRANCH, NDMNAME, LOGINNAME from NDM) as NDM
on stockinfo.audtorg=NDM.BRANCH
group by LOGINNAME
order by LOGINNAME"""
data = pd.read_sql_query(query, connection)

x = data['LOGINNAME'].tolist()
y = data['Stock'].tolist()

fig, ax = plt.subplots(figsize=(12, 4.8))
ax.plot(x, y, label='Stock', color='red', marker='o')
# ax.plot(x, z, color='blue', marker='o')

plt.xlabel("NDM Name", color='black', fontsize=12, fontweight='bold')

plt.ylabel("Stock", color='black', fontsize=12, fontweight='bold')
plt.yticks(np.arange(0, max(y) + 100, 50))
plt.title('NDM wise MTD stock', fontweight='bold', color='black', fontsize=18)
ax.legend(loc='best')

for a, b in zip(x, y):
    plt.text(a, b, str(b) + 'K', ha='center', va='bottom', rotation=45)

plt.tight_layout()
# plt.savefig('T4.png')
print('complete')
plt.show()
