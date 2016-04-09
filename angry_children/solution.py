k = int(raw_input())
n = int(raw_input())

arr = []
for i in range(n):
    arr.append(int(raw_input()))
    
l = sorted(arr)
unfairness = l[k-1] - l[0]
    
for i in range(1, len(arr)-k):
    unfairness = min(unfairness, l[i+k-1] - l[i])

print unfairness