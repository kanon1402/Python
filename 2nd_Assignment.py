


list = [20, 40, 20, 2, 10, 14, 55, 80, 3, 90]
print ('My List is: ', list)
list.insert(4,2020)
print ('After Insert My List is: ', list)
list2 = [6,12]
print ('Another List is: ', list2)
bothlist = list+list2
print ('After Adding both List is: ', bothlist)
print('Size of total list: ', len(bothlist))
bothlist.sort(reverse=True)
print('Descending list is: ', bothlist)
print('Maximum Number in list is: ', max(bothlist))
print('Minimum Number in list is: ', min(bothlist))


