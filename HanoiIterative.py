n = 16
a = []
b = []
c = []
movs = pow(2, n)

for i in range(1, n+1):
    a.append(i)
print("torre inicial a=", a, "torre final c=", c)


def reco(x):
    r = len(x)
    for j in range (0, r-1):
        x[j] = x[j+1]
    if len(x)>=1:
        x.pop()


def swapDisc(y, z):
    if (len(y)==0):
        print("Mueve el disco",z[0],"a torre 1", str("%y"))
        temp = z[0]
        y.insert(0, temp)
        reco(z)

    elif ((len(z) == 0) or (y[0] < z[0])):
        print("Mueve el disco", y[0], "a torre 2", str("%z"))
        temp = y[0]
        z.insert(0, temp)
        reco(y)

    else:
        print("Mueve el disco",z[0],"a torre 3", str("%y"))
        temp = z[0]
        y.insert(0, temp)
        reco(z)





for i in range (1, movs):

    if i%3 == 1:
        swapDisc(a, c)

    if i%3 == 2:
        swapDisc(a, b)

    if i%3 == 0:
        swapDisc(b, c)

if n%2==0:
    c=b
    b=[]

print("torre inicial a=", a, "torre final c=", c)