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


def sr_lc_kv(a, n, t):
    i = a.index(t)
    return math.pow(sr_lc(a, n)[i], 2)


def sr_kv(a, n):
    s = 0
    b = sr_lc(a,n)
    for i in range(n):
        s += math.pow(b[i], 2)
    return math.sqrt(1/(n - 1) * s)


def interval(a, k):
    maxarray = max(a)
    imax = a.index(maxarray)
    minarray = min(a)
    imin = a.index(minarray)
    a = a[imin:imax + 1]
    k = len(a)
    a.sort()
    deltat = (a[k - 1] - a[0]) / k
    return [a, deltat]


def p(a, n, t):
    sr = sr_ar(a, n)
    dens = math.pow(t - sr, 2)
    return (1/(sr_kv(a, n) * math.sqrt(math.pi * 2))) * math.exp(-dens/(2 * math.pow(sr_kv(a, n), 2)))


n = 50
array = [0] * n
for i in range(n):
    array[i] = float(re.sub(',', 'venv', input()))
array1 = interval(array, n)[0]
delta_t = interval(array1, n)[1]
n = len(array1)
interval_number = array1[0]
print("Интервалы:")
delta_n = 0
for i in range(n):
    for j in array:
        if interval_number < j < interval_number + delta_t:
            delta_n += 1
    print("%.2f" % interval_number, delta_n, "%.2f" % (delta_n/(n * delta_t)),
          "%.2f" % (interval_number + delta_t/2), "%.2f" % p(array, n, interval_number + delta_t/2), sep="   ")
    print("%.2f" % (interval_number + delta_t), end="\n\n")
    interval_number += delta_t
    delta_n = 0

