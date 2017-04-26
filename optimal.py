# This file contains the function for the Optimal page replacement algorithm.

# optimal runs the Optimal page replacement algorithm on input with the
# number of frames also as a paramter, and returns the number of faults.
def optimal(input, frames):
	pages = [] # Pages stored from input
	faults = 0 # Number of page faults

	for page in input:
		if not page in pages:
			faults += 1

			if len(pages) < frames:
				pages.append(page)
			else:
				i = 1
				least = 0
				while i < len(pages):
					if input.count(pages[i]) < input.count(pages[least]):
						least = i
				pages[least] = page

		input.remove(page)

	return faults
