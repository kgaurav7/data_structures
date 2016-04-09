'''
# Read input from stdin and provide input before running if required
data = raw_input()
print 'I Read, %s.' % data
'''
#Enter Your Code Here
inputlist = raw_input().split()
n = int(inputlist[0])
W = int(inputlist[1])

v = []
w = []
vperunitwt = []
for i in range(n):
    item = raw_input().split()
    v.append(int(item[0]))
    w.append(int(item[1]))
    vperunitwt.append((i, float(v[i])/w[i]))
    
vperunitwt = sorted(vperunitwt, key=lambda x: x[1], reverse = True)

V = 0
remWt = W
for i in range(n):
    if not remWt:
        break
    a = min(remWt, w[vperunitwt[i][0]])
    
    V += a * vperunitwt[i][1]
    remWt -= a
print int(V)