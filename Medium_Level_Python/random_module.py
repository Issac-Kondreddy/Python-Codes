import random
num=random.random()
print(num)


num = random.randint(1, 500)
print( num )


num = random.randrange(1, 10)
print( num )
num = random.randrange(1, 10, 2)
print( num )

random_s = random.choice('Random Module') #a string
print( random_s )
random_l = random.choice([23, 54, 765, 23, 45, 45]) #a list
print( random_l )
random_s = random.choice((12, 64, 23, 54, 34)) #a set
print( random_s )

list1 = [34, 23, 65, 86, 23, 43]
random.shuffle( list1 )
print( list1 )
random.shuffle( list1 )
print( list1 )    