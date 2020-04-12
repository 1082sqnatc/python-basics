greeting = 'Hello '
multiplier = 3
newname = 'something'
names = []
while newname:
    print('Please enter a name (leave blank when done):-')
    newname = input()
    # Don't add a blank name!
    if newname:
        names.append(newname)

allthepeople = ''

#for nameIndex in range(len(names)): # Works in most languages
for nameIndex, name in enumerate(names): # Very pythonic alternative
    if nameIndex > 0 :
        allthepeople = allthepeople + ' and '
    allthepeople = allthepeople + name # or names[nameIndex]

print(greeting * multiplier + allthepeople + '!')
