choices = input("Type your choices, separated by a comma:  " )
choice = choices.split(',')
#print(choice)
for c in choice:
    print(c + " = '" + c + "'")

for c in choice:
    print('(' +  c + ' , "' + c + '"),')
