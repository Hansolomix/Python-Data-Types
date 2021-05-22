'''
Text Type (String)
'''

s = 'This is the single line string'
print(s)
print(type(s))

# =========

s = '''This is the multi line
string example'''
print(s)
print(type(s))

#  ========

# find a character by index

s = 'string sample'
print(s[5])

# slicing

s = 'string sample'
print(s[7:])
print(s[0:7])

# # immmutable ( cannot change something in string ) error will show
# s = 'string sample'
# s[2] = o
# print(s) 

'''
Numeric Type ( Interger, Float , Complex )
'''
x = 123456789
print(type(x))

x = 0.0123456789
print(type(x))

x = 1+2j
print(type(x))

'''
Sequence Type ( List , Tuple , Range )
'''
# list ===  starts with [ ]
# homogeneous

x = [ 10 , 2.5 , 'hello' ]
print(x[1])
print(x[1:3])

#  mutable ( can change something in list )
x[2] = 'Python'
print(x)

#  Tuple ==== starts with ( )
#  heterogeneous

tuple = ()
tuple = ( "cat" , [1,2,3], [ 3,2,1 ] )
print(tuple)

# examples belows are type tuples.. adding , will make tuple... without , willl make string

tuple = ("hello"),
tuple = ("hello",)
tuple = "hello",
print(type(tuple))

# ===========

tuple = ("cat" , [4,3,2] , (1,2,3))
print(tuple[2])

# =========

# immmutable

#tuple = ( "cat" , [4,3,2] , (3,2,1))
#tuple[2] = 10
# it will show error ( tuple cannot change something in the list )

# ==========

# range

x = range(10)
for n in x:
 print(n)

""""
 Mapping Type ( Dictionary )
"""

# dict = {}
# print(type(dict))

 # ==========

# dict is mutable
dict = {'name': 'Kingsley', 'age':37}
print(dict['age'])
print(dict.get('name'))

dict['age'] = 26
print(dict)

# ========

'''
Set Types
'''

# emtpty set having set = {} is an empty dict

set = set()
print(type(set))

# ====================

# mixed data types ( all immutable )

#set = {3.2, "hi", (1,2,3)}
#print(type(set))
#TypeError: 'set' object is not subscriptable
#print(set[0])

# ====================

# no duplicates

set = {3.2, "hi", (1,2,3), "hi"}
print(set)

# ====================

# cannot have mutable (list) in a set
#set = {3.2, "hi", (1,2,3), [1,2,3]}
# unhashable type: 'list'
#print(set)

'''
Boolean Type (True or False)
'''

print(type(True))

# boolean as numbers
print(True == 1)
print(False == 0)

# interesting logic
print(True + True)

# not boolean operator
print(not True)
print(not False)

# and boolean operator
print(True and False)
print(True and True)
print(False and False)

#or boolean operator
print(True or False)
print(True or True)
print(False or False)
































