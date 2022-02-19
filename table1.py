import math
import re

def sr_ar(a, n):
    s = 0
    for i in range(n):
        s += a[i]
    return s/n


def sr_lc(a, n):
    sr = sr_ar(a, n)
    b = []
    for i in range(n):
        b.append(a[i] - sr)
    return b

def sr_lc_kv(a, n, i):
    return math.pow(sr_lc(a, n)[i], 2)


def sr_kv(a, n):
    s = 0
    b = sr_lc(a,n)
    for i in range(n):
        s += math.pow(b[i], 2)
    return math.sqrt(1/(n - 1) * s)


def interval(a, n):
    maxarray = max(a)
    imax = a.index(maxarray)
    minarray = min(a)
    imin = a.index(minarray)
    a = a[imin:imax + 1]
    n = len(a)
    a.sort()
    deltat = (a[n - 1] - a[0]) / n
    return a, deltat


n = 50
array = [0] * n
for i in range(n):
    array[i] = float(re.sub(',', 'venv', input()))
n = len(array)

print("Колонки: ")
for i in range(n):
    print("%.2f" % array[i], "%.2f" % sr_lc(array, n)[i], "%.2f" % sr_lc_kv(array, n, i), sep="   ")
print("Среднее арифмитическое: " + "%.2f" % sr_ar(array, n))
print("Сумма второй колонки: ", "%.2f" % sum(sr_lc(array, n)))
print("Среднее квадратичное: " + "%.2f" % sr_kv(array, n))
p_max = 1/sr_kv(array, n) * math.sqrt(math.pi * 2)



