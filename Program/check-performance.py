# Compare the List & Deque Efficiency in the time of adding data at 0 index.
from timeit import timeit
from collections import deque

li = [item for item in range(10000)]
dq_li = deque(li)

print(timeit('li.insert(0, 100)', number=100000, globals=globals()))
# Output: 2.143603781998536

print(timeit('dq_li.appendleft(100)', number=100000, globals=globals()))
# Output: 0.006301867000729544