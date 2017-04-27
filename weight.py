# This file implements the Weighted algorithm, where pages are removed based
# on a weight of frequency and most recent.

# calcWeight takes pages and stats and returns weights based
# on the stats.
def calcWeights(pages, stats, freqWeight, timeWeight):
	weights = [None]*len(pages) # Eventual weights list to return. Parallel to pages. Initialized to access elements out of order later.
	values = [] # Values to be weighed. Parallel to pages.
	weight = len(pages) # Initialize maximum weight.

	# Calculate values for weighing.
	for page in pages:
		values.append(freqWeight * stats[page][0] + timeWeight * stats[page][1])

	# Weigh the values.
	i = 0
	while i < len(pages):
		maxI = values.index(max(values))
		values[maxI] = None
		
		weights[maxI] = weight
		weight -= 1
		
		i += 1

	return weights
			

# weighted algorithm will remove pages based on a weight calculated with
# frequency and timestamp.
def weight(input, frames, freqWeight, timeWeight, doPrint):
	# Print header.
	if doPrint:
		print 'Weighted, Frames: {}, FreqWeight: {}, TimeWeight: {}'.format(frames, freqWeight, timeWeight)
	
	pages = [] # Pages stored from input
	stats = {} # Frequencies and timestamps for the pages in input
	faults = 0 # Number of page faults
	time = 1 # Time for timestamps
	uniquePages = len(set(input))

	# Initialize stats for pages in input.
	for page in set(input):
		stats[page] = [0, 0]

	for page in input:
		# Increment frequency and set timestamp.
		stats[page][0] += 1
		stats[page][1] = time

		if not page in pages:
			faults += 1
			
			if len(pages) < frames:
				pages.append(page)
			else:
				leastI = 0
				weights = calcWeights(pages, stats, freqWeight, timeWeight)

				i = 1
				while i < len(weights):
					if weights[i] < weights[leastI]:
						leastI = i
					i += 1

				pages[leastI] = page

		# Increment time.
		time += 1

		# Print status of pages.
		if doPrint:
			print pages
				
	return faults
