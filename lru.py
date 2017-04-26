# Least Recently Use
# This algorithm takes out the least recently used page

def lru(input, frames):
	pages = [] # Pages stored from input
	stamps = {} # Time stamps of pages in input.
	faults = 0 # Number of page faults
	time = 1
	
	# Initialize stamps for each page in input.
	for page in set(input):
		stamps[page] = 0

	for page in input:
		print("page", page)
		
		stamps[page] = time

		print("Times", stamps)
		
		if not page in pages:
			faults += 1

			if len(pages) < frames:
				pages.append(page)
			else:
				least = 0
				i = 1
				while i < len(pages):
					if stamps[pages[i]] < stamps[pages[least]]:
						least = i
					i += 1

				pages[least] = page

		print("pages", pages)
		time+=1
		
	return faults
	
