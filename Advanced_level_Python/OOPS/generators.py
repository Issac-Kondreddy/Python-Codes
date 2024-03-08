def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

for value in gen:
    print(value)


gen_exp = (x * 2 for x in range(3))

for value in gen_exp:
    print(value)
