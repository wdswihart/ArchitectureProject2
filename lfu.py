# lfu contains the Least Frequently Used (LFU) algorithm for avoiding page # faults.

# lfu runs the LFU page replacement algorithm on input with the
# number of frames also as a paramter, and returns the number of faults.
def lfu(input, frames):
	pages = [] # Pages stored from input
	freq = {} # Frequencies of pages in input.
	faults = 0 # Number of page faults

	# Initialize frequencies for each page in input.
	for page in set(input):
		freq[page] = 0

	for page in input:
		freq[page] += 1

		if not page in pages:
			faults += 1

			if len(pages) < frames:
				pages.append(page)
			else:
				least = 0
				i = 1
				while i < len(pages):
					if freq[pages[i]] < freq[pages[least]]:
						least = i
					i += 1

				pages[least] = page

	return faults
