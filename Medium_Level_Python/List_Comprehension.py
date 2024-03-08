names = ['Issac','Bharadwaj','Tharun', 'Vikram','Pranay','Nandha']
newlist =[x for x in names if 'y' in x or 'i' in x or 'I' in x]
print(newlist)

numbers = [1,2,3,4,5,6,7,8]
squares = [x**3 for x in numbers]
print(squares)

#iteration through String

name = 'Issac'
print([x for x in name])