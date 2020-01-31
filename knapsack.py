def knapsackBF(items, maxW, n):
	if(maxW ==0 or n==0):
		return 0
	if(items[n-1].weight > maxWeight):
		return knapsackBF(items,maxWeight, n-1)
	else:
		return max(items[n-1].value + knapsackBF(items, maxWeight-items[n-1].weight, n-1), knapsackBF(items, maxWeight, n-1))

#Time Complexity O(nlogn)
#Space Complexity O(n)

def knapsackTab(items, maxW, n):
	table = [[0 for x in range(maxW +1)] for x in range(n+1)]

	for i in range(n+1):
		for w in range(maxW + 1):
			if (i==0 or w==0):
				table[i][w] = 0
			elif (items[i-1].weight <= w):
				table[i][w] = max(items[i-1].value + table[i-1][w-items[i-1].weight], table[i-1][w])
			else:
				table[i][1] = table[i-1][w]

	return table[n][maxW]

#Time Complexity O(n^2)
#Space Complexity O(n)

def knapsackMemo(items,maxW, n, table):
	if(maxW==0 or n == 0):
		return 0

	if(items[n-1].weight > maxW):
		return knapsackMemo(items, maxW, n-1, table)
	elif(table[n][maxW] != 0):
		return table[n][maxW]
	else:
		table[n][maxW] = max(items[n-1].value + knapsackMemo(items, maxWeight-items[n-1].weight, n-1, table), knapsackMemo(items, maxWeight, n-1, table))	
		return[n][maxW] 

#Time Complexity O(n)
#Space Complexity O(n^2)

class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight








