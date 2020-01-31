#Funky numbers

#(Extracted from https://codeforces.com/problemset/problem/192/A)

#As you very well know, this year's funkiest numbers are so called triangular numbers (that is, integers that are representable as k(k+1)2\frac{k(k+1)}{2}2k(k+1)​ , where k is some positive integer), and the coolest numbers are those that are representable as a sum of two triangular numbers.

#A well-known hipster Andrew adores everything funky and cool but unfortunately, he isn't good at maths. Given number n, help him define whether this number can be represented by a sum of two triangular numbers (not necessarily different)!

#Inputs:

 #   The first input line contains an integer n (1 ≤ n ≤ 109)

#Outputs

#    Print "YES" (without the quotes), if n can be represented as a sum of two triangular numbers, otherwise print "NO" (without the quotes).

def binarySearch (arr, l, r, x): 
    if r >= l:
        mid = int(l + (r - l)/2)
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else: 
        return -1
    
n = int(sys.stdin.readline())
trianNumbers = []
loop = True
i = 1

while(loop):
    tri = i * (i+1) / 2
    if i > n:
        loop = False
    trianNumbers.append(tri)
    i = i + 1

found = False
for x in trianNumbers : 
        if((binarySearch(trianNumbers,0,len(trianNumbers)-1,n-x))==-1):
               found = False
        else:
               found = True
               break

if(found):
    print("YES")
else:
    print("NO")