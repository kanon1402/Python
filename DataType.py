# # Basic Data Types
# Number(Integer, Floating), Sequence(String, List, Tuple)

# # # Number -> Integer ----------------------------------
#
production_cost = 2000
distribution_cost = 500
tax = 100.52342353
overall_sales = 5000
#
# print('Production Cost = ', production_cost)
# print('Production Cost Data Type = ', type(production_cost))
#
#
# # # Number -> Floating --------------------------------
# print('Tax = ', tax)
# print('Tak Data Type = ', type(tax))
# # Limiting floating point number
# print('Two decimal point = ', round(tax, 2))
# print('Two decimal point = ', "{:.2f}".format(tax))

# # Sequence -> String -------------------------------
# first_name = "Alhama Ekbal"
# last_name = 'Kanon'

# print('First Name = ', first_name)
# print(type(first_name))
# print('Last Name = ', last_name)
# print(type(last_name))


# # Join String ---------------------------------------
# full_name = first_name + last_name
# print('Full Name = ', full_name)
#
# # String Concatenation
# full_name = first_name + ' ' + last_name
# print('Full Name = ', full_name)
# print('Full Name = ', first_name + ' ' + last_name)

# sales = 404834
# print(sales)
# print('Sales is: ' + str(sales) + 'Tk.')
# print('Sales is: ', sales, 'Tk.')


# # # Sequence-> List------
blank_list = []
num_list = [1, 2, 35, 7, 4, 6, 4, 6, 64, 3, 2]
name_list = ['Sagir', 'Kanon', 'BM. Ashik', "Royel", 'Rabby']
multiple_data = [10, 20, 4, 'Twelve', 6.123456, 'Orange']

# print(num_list)
# print(name_list)
# print(num_list+name_list)


# Index--------------------------
# print(num_list[0])
# print(num_list[0:4])
# print(num_list[:2])
# print(num_list[2:6])


# # # Arithmetic Operation in List-----------
# first = num_list[0]
# second = num_list[1]
# third = first + second
# print(third)

# # # Nested list------------------
# nested_list = [['A','B'], [5,10]]
#
# print(nested_list[0])
# print(nested_list[0][1])
# print(nested_list[1][1])

# # # -------------------List Operation----------------------
# # Insert item in the list-----------
# print('Our Number List = ', num_list)
# num_list.append(30)
# print(num_list)
# num_list.extend([100,200,300])
# print(num_list)

# # Sequence => Tuple---------------------------------
# # Tuple is faster than list but you can not insert an element in the tuple

tuple = ('This', 'is', 'a', 'Tuple')
print('Tuple = ', tuple)
print('Type is = ', type(tuple))

print(tuple[0])