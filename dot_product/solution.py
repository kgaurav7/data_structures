n = int(raw_input())
astr = raw_input().split()
bstr = raw_input().split()

a = [int(x) for x in astr]
b = [int(x) for x in bstr]

a = sorted(a, reverse=True)
b = sorted(b)

result = 0
for i in range(len(a)):
    result += a[i] * b[i]
print result