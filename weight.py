# This file implements the Weighted algorithm, where pages are removed based
# on a weight of frequency and most recent.

# weighted algorithm will remove pages based on a weight calculated with
# frequency and timestamp.
def weight(input, frames):
	pages = [] # Pages stored from input
	stats = {} # Frequencies and timestamps for the pages in input
	faults = 0 # Number of page faults
	time = 1 # Time for timestamps
	uniquePages = len(set(input))

	# Initialize stats for pages in input.
	for page in set(input):
		stats[page] = (0, 0)

	for page in input:
		# Increment frequency and set timestamp.
		stats[page][0] += 1
		stats[page][1] = time
		
		if not page in pages:
			if len(pages) < frames:
				pages.append(page)
			else:
				leastI = 0
				leastWeight = 1.3 * stats[pages[0]][0] + stats[pages]

				i = 1
				while i < len(pages):
					
				
	return faults
