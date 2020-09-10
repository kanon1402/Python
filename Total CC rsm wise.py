import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def convert(number):
    number = int(number / 1000)
    number = format(number, ',')
    number = number + 'K'
    return number


connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHND;'
                        'UID=sa;PWD=erp@123')

query = """

declare @todate varchar(8) = CONVERT(varchar(8), dateAdd(day,0,getdate()), 112)
declare @ystdate varchar(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
declare @1stdate varchar(8) = CONVERT(varchar(8), DATEADD(DAY, 1, EOMONTH(getdate(), -1)), 112)
declare @date varchar(6) = CONVERT(varchar(6), dateAdd(day,0,getdate()), 112)

select RSMNAME, TotalCust from 
(select RSMTR, COUNT(DISTINCT CUSTOMER) as TotalCust from OESALESDETAILS
where TRANSDATE between @1stdate and @ystdate and RSMTR is not null and RSMTR <> '0' and RSMTR <> 'ZREGION'
group by RSMTR) as t1
left join
(select DISTINCT RSMTR, RSMNAME from V_RFieldForce
where YEARMONTH = @date and RSMTR not like '%INS%') as t2
on t1.RSMTR=t2.RSMTR
where RSMNAME is not null
order by RSMNAME

"""

x = pd.read_sql_query(query, connection)
y = x['RSMNAME'].tolist()
data = x['TotalCust'].tolist()
# print(data)

# A = 3000
# B = 4000
#
# data = [A, B]
total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6] + data[7] + data[8]
total = 'Total \n' + str(convert(total))
print(data)
print(total)

colors = ['#f9ff00', '#ff8600', '#5d87a3', '#cadb2a', '#c085e9', '#228b22', '#addcca'
    , '#33ffff', '#d0acff']
legend_element = [Patch(facecolor='#f9ff00', label='Akhter'),
                  Patch(facecolor='#ff8600', label='Atik'),
                  Patch(facecolor='#5d87a3', label='Byron'),
                  Patch(facecolor='#cadb2a', label='Koushik'),
                  Patch(facecolor='#c085e9', label='Pradip'),
                  Patch(facecolor='#228b22', label='Rubel'),
                  Patch(facecolor='#addcca', label='Shafiq'),
                  Patch(facecolor='#33ffff', label='Shakib'),
                  Patch(facecolor='#d0acff', label='Shohel')
                  ]

# A = convert(data[0])
# B = convert(data[1])
# Data_label = [A, B]

fig, ax = plt.subplots(figsize=(6.4, 4.8))
pack_all, label, percent_value = ax.pie(data, labels=data, colors=colors,
                                        autopct='%.1f%%',
                                        textprops={
                                            'color': "Black"}, startangle=90, pctdistance=.80)

plt.setp(percent_value, fontsize=14, color='blue', fontweight='bold')
plt.setp(label, fontsize=14, fontweight='bold')

ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold')
centre_circle = plt.Circle((0, 0), 0.40, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('RSM Wise Covered Customer', fontsize=18, fontweight='bold', color='#3e0a75', pad='15.0')
ax.axis('equal')
plt.legend(handles=legend_element, loc='best', fontsize=11, bbox_to_anchor=[0.9, 1.10])
plt.tight_layout()
plt.savefig('TotalCoveredChemistRsmWise.png')
plt.show()
