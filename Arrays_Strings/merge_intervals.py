''' 
WAP to merge two list of sorted intervals into one single non-overlapping intervals. The intervals are sorted w.r.t the starting time.

I/P: ListA : [(-3, -1), (0, 1), (2, 3)]
     ListB : [(-4, 1), (1, 1.5), (4, 6)]

O/P: Final : [(-4, 1.5), (2, 3), (4, 6)]
'''

class MergeInterval:

	def merge_intervals(self, listA, listB):
		'''
		This method will merge the given intervals into one single non-overlapping list.
		'''
		final_list = []
		startA, startB, endA, endB = 0, 0, len(listA), len(listB)
		start, end = None, None
		while startA < endA and startB < endB:
			#Checking if I need to select a new interval
			if not start:
				#Checking if current intervals are overlapping
				if listA[startA][0] in range(listB[startB][0], listB[startB][1]+1) or listB[startB][0] in range(listA[startA][0], listA[startA][1]+1):
					start, end = min(listA[startA][0], listB[startB][0]), max(listA[startA][1], listB[startB][1])
				else:
					if listA[startA][0] < listB[startB][0]:
						final_list.append(listA[startA])
						final_list.append(listB[startB])
					else:
						final_list.append(listB[startB])
						final_list.append(listA[startA])
				startA += 1
				startB += 1
			else:
				#Add the merged interval to the final list and start looking for a new interval
				if end < listA[startA][0] and end < listB[startB][0]:
					final_list.append((start, end))
					start, end = None, None
				else:
					if listA[startA][0] <= end:
						end = max(end, listA[startA][1])
						startA += 1
					if listB[startB][0] <= end:
						end = max(end, listB[startB][1])
						startB += 1
		#Checking if there is an interval left to be added
		if start:
			final_list.append((start, end))
		#Checking if there are some intervals left in the first set
		while startA < endA:
			final_list.append(list[startA])
			startA += 1
		#Checking if there are some intervals left in the second set
		while startB < endB:
			final_list.append(listB[startB])
			startB += 1
		return final_list

if __name__ == '__main__':
	merge = MergeInterval()
	listA = [(-3, -1), (0, 1), (2, 3)]
	listB = [(-4, 1), (1, 2), (3, 6)]
	print(merge.merge_intervals(listA, listB))