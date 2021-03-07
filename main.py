
# # add 'Tee' to variable 'name'
# name="Tee"
# print(name)

#============================

# # assign same values to multiple variables on the same line 
# a=b=c='cat' 
# print(a)
# print(b)
# print(c)


# #============================
#  reuse variable names, the last assignment is printed
 
# colour ='Red'
# colour ='Blue'
# print(colour)

# #============================


# # legal variable names

# firstname="John"
# first_name="John"
# firs_tname="John"
# firstName="John"
# firstname2="John"
# FIRSTNAME="John"
# _first_name="John"


#============================

# illegal variable names

# first-name="John"
# first name="John"
# 2firstname="John"

#============================
# ''''
# Reserved Keywords
# ''''
# help('keywords')

# ====================

# variable types
# var= 'Hello World'
# print(type(var))

# var = 40
# print(type(var))

# ====================
'''
object identity
'''
# score = 400
# identity= id(score)
# print(identity)

# score variable is saved into the pb by reference
# score = 400
# pb=score
# print(id(score))
# print(id(pb))
#===========================
# ''''
# Object Reference
# ''''
# both pb and score referencing the same object
# pb----> int 100<----score
# score =100
# pb=score
# print(pb)
# print(score)
# print(type(score))
# print(type(pb))

#===========================
#  pb---------------> 20
#  score------------>100

# pb=20
# score=100
# print(type(score))
# print(type(pb))
# print(score)
# print(pb)

# garbage collection
# pb---------->int 20
# score------------> str'Completed'
# ------------->int 100
pb=20
score=100
score='Completed'

print(type(score))
print(type(pb))
print(pb)
print(score)
