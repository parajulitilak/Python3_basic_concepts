'''
we do curly bracket in python not to wrap a block of codes like in c,js,php
we do this only to define a dictionary in python.
{"key":"values","key":"values"....................}
'''

mydict={"Name":"Tilak","Surname":"Parajuli","Age":"23","Hobby":"Coding"}
print(mydict)

'''the above print line will print 
{'Name': 'Tilak', 'Surname': 'Parajuli', 'Age': '23', 'Hobby': 'Coding'}
'''

print(mydict['Name'])
#the above print will print Tilak.

print(mydict['Surname'])
#the above print will print Parajuli.

print(mydict['Age'])
#the above print will print 23.

print(mydict['Hobby'])
#the above print will print Coding.