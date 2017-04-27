import optimal
import fifo
import lfu
import lru
import weight

# test prints a test run of each algorithm with a given input and frame count.
def test(input, frames, doPrint):
	print 'Optimal', optimal.optimal(input[:], frames, doPrint)
	print 'FIFO', fifo.fifo(input, frames, doPrint)
	print 'LRU', lru.lru(input,frames, doPrint)
	print 'LFU', lfu.lfu(input, frames, doPrint)
	print 'Weighted', weight.weight(input, frames, 4, 1, doPrint)

# Run algorithms for 3 and 4 frames on a basic input and print the results.
doPrint = True # Whether or not to print results to the console.
input = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] # List that the algorithms will run on.
frames = 3 # Number of frames for the pages list.
while frames < 5:
	print 'Page faults: {}\n'.format(optimal.optimal(input, frames, doPrint))
	print 'Page faults: {}\n'.format(fifo.fifo(input, frames, doPrint))
	print 'Page faults: {}\n'.format(lru.lru(input,frames, doPrint))
	print 'Page faults: {}\n'.format(lfu.lfu(input, frames, doPrint))

	# Run Weighted with increasing frequency multipliers.
	i = 1 # Loop variable, and frequency multiplier for Weighted.
	while i < 10:
		print 'Page faults: {}\n'.format(weight.weight(input, frames, i, 1, doPrint))
 
		i += 1

	frames += 1

# Get input data.
input = [] # Reset input.

with open('project_input.txt',  'r') as file:
	lines = file.read().strip().split('\n')

	for line in lines:
		input.append(int(line))

# Run algorithms for 3, 4, 5, 6, and 7 frames and store the results.
doPrint = True
frames = 3 # Reset frames to 3.
optimalFaults = []
fifoFaults = []
lruFaults = []
lfuFaults = []
weightedFaults = []

while frames < 8:
	optimalFaults.append(optimal.optimal(input, frames, doPrint))
	fifoFaults.append(fifo.fifo(input, frames, doPrint))
	lruFaults.append(lru.lru(input, frames, doPrint))
	lfuFaults.append(lfu.lfu(input, frames, doPrint))

	# Run Weighted with increasing frequency multipliers.
	faults = [] # Page faults for the Weighted runs on this frame size.
	
	i = 1 # Loop variable, and frequency multiplier for Weighted.
	while i < 11:
		faults.append(weight.weight(input, frames, i, 1, doPrint))
		i += 1

	weightedFaults.append(faults)

	frames += 1

# Output results for frames 3, 4, 5, 6, and 7 on the big input.
with open('results.txt', 'w') as file:
	file.write('Optimal:\n3 Frames: {}\n4 Frames: {}\n5 Frames: {}\n6 Frames: {}\n7 Frames: {}\n\n'.format(optimalFaults[0], optimalFaults[1], optimalFaults[2], optimalFaults[3], optimalFaults[4]))
	file.write('FIFO:\n3 Frames: {}\n4 Frames: {}\n5 Frames: {}\n6 Frames: {}\n7 Frames: {}\n\n'.format(fifoFaults[0], fifoFaults[1], fifoFaults[2], fifoFaults[3], fifoFaults[4]))
	file.write('Least Recently Used:\n3 Frames: {}\n4 Frames: {}\n5 Frames: {}\n6 Frames: {}\n7 Frames: {}\n\n'.format(lruFaults[0], lruFaults[1], lruFaults[2], lruFaults[3], lruFaults[4]))
	file.write('Least Frequently Used:\n3 Frames: {}\n4 Frames: {}\n5 Frames: {}\n6 Frames: {}\n7 Frames: {}\n\n'.format(lfuFaults[0], lfuFaults[1], lfuFaults[2], lfuFaults[3], lfuFaults[4]))

	file.write('Weighted:\n')
	
	i = 3
	while i < 8:
		file.write('{} Frames:\n'.format(i))

		j = 0
		while j < 10:
			file.write('FreqWeight {}: {}\n'.format(j+1git p, weightedFaults[i-3][j]))
			j += 1

		i += 1









	
