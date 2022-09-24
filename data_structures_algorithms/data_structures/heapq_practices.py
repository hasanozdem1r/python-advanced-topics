# heap rules
# h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2]
# https://realpython.com/python-heapq-module/
import heapq as hq

# convert array to heap
ar = [3, 5, 1, 2, 6, 8, 7]
hq.heapify(ar)
print(ar)

# pop element
hq.heappop(ar)
print(ar)

# push element
hq.heappush(ar, 4)
print(ar)
