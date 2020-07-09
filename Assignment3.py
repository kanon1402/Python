# Assigned Problem 01:
# -----------------------------------------------------------------------
# Data_list = [1, 5, 3, 9, 7, 8, 2, 6]
# Test_value = 7
# if Test_value in Data_list:
#     for x in Data_list:
#         # print(x)
#         if x < Test_value:
#             print(Test_value, 'is greater than ', x)
#         elif x > Test_value:
#             print(Test_value, 'is smaller than ', x)
#         else:
#             print('Same value')

# -----------------------------------------------------------------------
# Assigned Problem 02:
# -----------------------------------------------------------------------

# Actual_Price = [10, 20, 30, 40, 50]
# Tax = [2, 4, 6, 8, 10]
#
# res_list = []
# for i in range(0, len(Actual_Price)):
#     res_list.append(Actual_Price[i] + Tax[i])
#
# print("list is : " + str(res_list))

# -----------------------------------------------------------------------
# Assigned Problem 03:
# -----------------------------------------------------------------------
def branch(str):
    branch_list = ['BARISAL', 'BHAIRAB', 'BOGRA', 'CHANDPUR', 'CHITTAGONG', 'COMMILLA', 'COXS BAZAR', 'CTG NORTH',
                   'DINAJPUR', 'FARIDPUR', 'FENI', 'GAZIPUR', 'JESSORE', 'KERANIGANJ', 'KHULNA', 'KISHOREGANJ',
                   'KUSTIA',
                   'MIRPUR', 'MOHAKHALI', 'MOTIJHEEL', 'MOULOVIBAZAR', 'MYMENSIGN', 'NARAYANGONJ', 'NOAKHALI', 'PABNA',
                   'PATUAKHALI', 'RAJSHAHI', 'RANGPUR', 'SAVAR', 'SYLHET', 'TANGAIL']

    if str in branch_list:
        print('Yes', str, 'is in branch list')
    else:
        print(str, 'Not Found in branch list')