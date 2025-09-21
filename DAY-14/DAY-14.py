my_dict={
    'name': 'rahul',
    'class': 'BCA',
    'marks':89
}
print(my_dict)

#deleteing data 
# del my_dict['class']
# print(my_dict)


#pop specific item
fname=my_dict.pop('name')
print(fname)

#pop
my_dict.popitem()
print(my_dict)

#getting data
print(my_dict.get("class"))

#copy
v=my_dict.copy()
print(v)