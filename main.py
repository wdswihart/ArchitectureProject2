import optimal
import fifo
import lfu
import lru
import weight

def test(input, frames):
	print("FIFO", fifo.fifo(input, frames))
	print("Optimal", optimal.optimal(input[:], frames))
	print("LFU", lfu.lfu(input, frames))
	print("LRU", lru.lru(input,frames))
	print("Weighted", weight.weight(input, frames))

input = []
frames = 5

with open("project_input.txt") as file:
	lines = file.read().strip().split("\n")

	for line in lines:
		input.append(int(line))

test(input, frames)
