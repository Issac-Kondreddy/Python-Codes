import collections
from collections import *

D = collections.OrderedDict()
D['A'] = 10
D['C'] = 12
D['B'] = 11
D['D'] = 13

for k, v in D.items():
    print(k, v)

c = Counter()
list = [1,2,4,7,5,1,6,7,6,9,1]
c = Counter(list)
print(c[1])
print(c[6])
print(c[7])


list_ = ["x","y","z"]
deq = deque(list_)
print(deq)
