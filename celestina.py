
def celestinaRec(n):
	if(n<=2):
		return (n + 1)
	else:
		return celestinaRec(n-1) +celestinaRec(n-2)*(n-1)

#Time Complexity O(nlogn)
#Space Complexity O(n)

def CelestinaTab(n):
	table = []
	for i in range(n+1):
		if (i<=2):
			table.append(i)
		else:
			table.append(table[i-1]+table[i-2]*(i-1))

	return table[n]

#Time Complexity O(n)
#Space Complexity O(n)

def celestinaMemo(n, table):
	if(n<=2):
		return n
	elif(table[n]!=0):
		return table[n]
	else:
		table.append(celestinaRec(n-1) +celestinaRec(n-2)*(n-1))
		return table[n]
		
#Time Complexity O(n)
#Space Complexity O(n)
