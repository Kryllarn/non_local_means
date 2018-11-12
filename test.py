from multiprocessing import Pool

def groscalcul(n):
    k = 0
    for i in range(n):
        k += i
    return k


pool = Pool()

nb = 30000000

args = [nb, nb + 10, nb*2]

res = pool.map(groscalcul, args)

for i in res:
    j = 1
    print("res",j, ":", i)
    j += 1