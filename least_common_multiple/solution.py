a = raw_input()
arr = a.split()

x = int(arr[0])
y = int(arr[1])

def gcd(c, d):
    if not d:
        return c
    return gcd(d, c % d)

print x * y / gcd(x, y)
