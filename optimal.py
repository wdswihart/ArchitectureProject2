# This file contains the function for the Optimal page replacement algorithm.

import copy

# optimal runs the Optimal page replacement algorithm on input with the
# number of frames also as a paramter, and returns the number of faults.
def optimal(input, frames, doPrint):
	# Print header.
	if doPrint:
		print 'Optimal, Frames: {}'.format(frames)
	
	pages = [] # Pages stored from input
	faults = 0 # Number of page faults
	temp = copy.deepcopy(input) # Copy input as to not modify original.

	for page in temp:
		if not page in pages:
			faults += 1

			if len(pages) < frames:
				pages.append(page)
			else:
				i = 1
				least = 0
				while i < len(pages):
					if temp.count(pages[i]) < temp.count(pages[least]):
						least = i
					i += 1
					
				pages[least] = page

		temp[temp.index(page)] = None

		# Print status of pages.
		if doPrint:
			print pages

	return faults
