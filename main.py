import optimal
import fifo
import lfu
import lru

input = [1,2,3,4,1,2,5,1,2,3,4,5]

#print(fifo.fifo(input, 5))
#print(optimal.optimal(input, 3))
#print(lfu.lfu(input, 3))
print(lru.lru(input,3))
