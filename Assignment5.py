import pandas as pd
import pyodbc as db
import numpy as np
from matplotlib import pyplot as plt

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=10.168.2.164;'
                        'DATABASE=ARCHND;'
                        'UID=sa;PWD=erp')

query = """

DECLARE @Thisday CHAR(8) = CONVERT(varchar(8), dateAdd(day,-1,getdate()), 112)
            DECLARE @lastday CHAR(8) = CONVERT(varchar(8), dateAdd(DAY,-2,getdate()), 112)
            DECLARE @thismonth CHAR(6) = CONVERT(varchar(6), dateAdd(MONTH,0,getdate()-30), 112)
            select top 9 RSMTR as RSMTR, 
            SUM(case when TRANSDATE = @Thisday then EXTINVMISC/1000 END)  as YesterdaySales,
            SUM(case when TRANSDATE = @lastday then EXTINVMISC/1000 END) as BeforeTwodaysSales,
            cast(SUM(case when transtype=2 and left(transdate,6) = @thismonth then (EXTINVMISC*(-1))/1000 END) as decimal(10,2)) as ReturnVal
            from OESalesDetails
            group by RSMTR
            order by  YesterdaySales desc,   BeforeTwodaysSales desc, ReturnVal DESC"""
data = pd.read_sql_query(query, connection)

x = data['RSMTR'].tolist()
day1_sale = data['YesterdaySales'].tolist()
day2_sale = data['BeforeTwodaysSales'].tolist()
t = data['ReturnVal'].tolist()
print(x)
print(day1_sale)
print(day2_sale)
print(t)

# def number_decorator(number):
#     number = round(number, 1)
#     number = format(number, ',')
#     number = number + 'K'
#     return number
#
#
# def thousand_K_number_decorator(number):
#     number = int(number / 1000)
#     number = format(number, ',')
#     number = number + 'K'
#     return number
#
#
# bar_index = np.arange(len(day2_sale))
#
# fig, ax = plt.subplots(figsize=(12.6, 6))
# opacity = 0.9
# bar1 = plt.bar(bar_index, day1_sale,
#                alpha=opacity, color='y', label='Frank')
#
#
# def autolabel(bar1):
#     for bar in bar1:
#         height = int(bar.get_height())
#         ax.text(bar.get_x(), height,
#                 number_decorator(height),
#                 va='bottom',
#                 fontsize=12, fontweight='bold')
#
#
# autolabel(bar1)
# ax.plot(x, t, color='red', marker='o')
#
# for a, b in zip(x, t):
#     plt.text(a, b, str(b) + 'K', ha='center', va='bottom')
#
# plt.ylabel('Sales Amount and Return')
# plt.xlabel('RSMTR Name')
# plt.title('Sales Evaluation - Developed by: Kanon')
# plt.xticks(bar_index, x)
#
# plt.legend(labels=('30 Days Return', 'Yesterday Sales'), loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True,
#            shadow=True, ncol=5)
#
# plt.tight_layout()
# plt.savefig('Assignment5.png')
# print('Complete')
# plt.show()
