s = raw_input()
sarr = s.split()

n = int(sarr[0])
m = int(sarr[1])

def fibonacci_adv(n, m):
    if not n:
        return 0
    if n == 1:
        return 1

    f = [0,1]
    i = 2

    while 1:
        f.append((f[i-1] + f[i-2]))
        if (f[i-1] + f[i-2]) % m == 1 and f[i-1] % m  == 0:
            break
        i += 1

    return (f[n % (i-1)]) % m 

print fibonacci_adv(n, m)
