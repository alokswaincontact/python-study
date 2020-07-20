#Doesn't work
#print(globals())

#print (type(globals()))

#Doesn't Work
#for i in (globals()):
#    print(i)
#Works
for i in tuple(globals()):
    print(i)

#Works
for i, v in dict(globals()).items():
    print(i, v)

print()

temp = globals()
#Works
for i in list(temp.keys()):
    print(i)

print()

#Works
for i in list(globals()):
    print(i)

print()

#Works
for i in list(temp.values()):
    print(i)
