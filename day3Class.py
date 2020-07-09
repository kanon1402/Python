# Basic Example

# number1 = 5
# number2 = 10
#
# if number1 >= number2:
#     print(number1, 'is grater than', number2)
# else:
#     print(number1, 'is either samller than or equal to = ', number2)


# # Example 2 ----------------

# name = 'Kanon'
# if name == 'BM. Ashiq':
#     print('Ashiq')
# elif name == 'Kanon':
#     print('Kanon')
# else:
#     print('I dont know who are you.')

# # Nested IF ----------------

employee_name_list = ['sagir', 'royel', 'kanon']
employee = 'sagir'
leave_take = 25
leave_allowed = 40

if employee in employee_name_list:
    print('Yes', employee, 'is an employee of Transcom')

    if leave_take > leave_allowed:
        print('He has no leave left')
    else:
        print('He has leave left = ', str(leave_allowed-leave_take), 'Days')
else:
    print(employee, 'is not an employee of Transcom')