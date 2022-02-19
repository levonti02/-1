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


def intervals(a, n):
    aver_t = sr_ar(a, n)
    sigma = sr_kv(a, n)
    return [[aver_t - sigma, aver_t + sigma],
            [aver_t - 2 * sigma, aver_t + 2 * sigma],
            [aver_t - 3 * sigma, aver_t + 3 * sigma]]


def amount_probability(a, n):
    aver_t = sr_ar(a, n)
    sigma = sr_kv(a, n)
    n1, n2, n3 = 0, 0, 0
    for i in a:
        if aver_t - sigma <= i <= aver_t + sigma:
            n1 +=1
        if aver_t - 2 * sigma <= i <= aver_t + 2 * sigma:
            n2 += 1
        if aver_t - 3 * sigma <= i <= aver_t + 3 * sigma:
            n3 += 1
    return [n1, n2, n3]


def probability(a, n):
    n1, n2, n3 = amount_probability(a, n)[0], amount_probability(a, n)[1], amount_probability(a, n)[2]
    return [n1 / n, n2 / n, n3 / n]


n = 50
array = [0] * n
for i in range(n):
    array[i] = float(re.sub(',', 'venv', input()))
print("%.2f" % intervals(array, n)[0][0], "%.2f" % intervals(array, n)[0][1],
      amount_probability(array, n)[0], "%.3f" % probability(array, n)[0], "0,683", sep="  ")
print("%.2f" % intervals(array, n)[1][0], "%.2f" % intervals(array, n)[1][1],
      amount_probability(array, n)[1], "%.3f" % probability(array, n)[1], "0,954", sep="  ")
print("%.2f" % intervals(array, n)[2][0], "%.2f" % intervals(array, n)[2][1],
      amount_probability(array, n)[2], "%.3f" % probability(array, n)[2], "0,997", sep="  ")
