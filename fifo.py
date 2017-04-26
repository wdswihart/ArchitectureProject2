#First in first out algorithm
#As the name suggests the algorithm takes in a list and the number of frames,
#creates a list the size of frames, and starts inserting the input into the frames,
#when the frames becomes full, the algorithm loops back and starts replacing the,
#first in if there is not a hit in the list

def fifo(input, frames):
	pages = []
	faults = 0
	first = 0

	for page in input:
		if not page in pages:
			faults+=1
			if len(pages)<frames:
				pages.append(page)
			else:
				pages[first] = page
				first += 1
				if first==frames:
					first = 0
	return faults
