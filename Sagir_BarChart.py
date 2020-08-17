import pandas as pd
import pyodbc as db
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

connection = db.connect('DRIVER={SQL Server};'
                        # 'SERVER=10.168.2.164;'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

query = """
select top 3  RTRIM(CAUSE) as CAUSE, CAST(SUM(val)/1000 as decimal(10,2)) as val from
(select Cause_Of_Return_ID, sum(INVNETH)*-1 as val from OESalesSummery
where transtype=2 and left(TRANSDATE,6) = 202006
group by Cause_Of_Return_ID) as t1
left join 
(select  * from OECauseOfReturn) as t2
on t1.Cause_Of_Return_ID=t2.CAUSEID
where CAUSE is not null
group by RTRIM(CAUSE)
order by val desc

"""


def number_decorator(number):
    number = round(number, 2)
    number = format(number, ',')
    number = number + 'K'
    return number


x = pd.read_sql_query(query, connection)
y = x['CAUSE'].tolist()
data = x['val'].tolist()
# print(data)
data_label = [number_decorator(data[0]), number_decorator(data[1]), number_decorator(data[2])]

# data_label = [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]]
# print(data_label)


#
#
colors = ['#778484', '#c0ffee', '#337f4e']
legend_element = [Patch(facecolor='#f9ff00', label='Canceled / Cash short'),
                  Patch(facecolor='#c085e9', label='Computer mistake'),
                  Patch(facecolor='#ff8600', label='Next day delivery')
                  ]

fig1, ax = plt.subplots(figsize=(12, 6))
pack_all, label, percent_value = ax.pie(data, labels=data_label, colors=colors,
                                        autopct='%.1f%%',
                                        textprops={'color': "Black"}, startangle=90, pctdistance=.70)

plt.setp(percent_value, fontsize=12, color='black', fontweight='bold')
plt.setp(label, fontsize=12)
plt.title('Top 3 Cause wise return for June month', fontsize=18, fontweight='bold', color='#3e0a75')
plt.legend(handles=legend_element, loc='best', fontsize=11)
ax.axis('equal')

plt.tight_layout()
plt.savefig('Sagir_Barchart.png')
# plt.show()
