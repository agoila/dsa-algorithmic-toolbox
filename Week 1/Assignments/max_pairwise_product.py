# Uses python3
import numpy as np

def max_pairwise_product_slow(n, a):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    return result


def max_pairwise_product_fast(n, a):
    max_index1 = -1
    for i in range(0, n):
        if max_index1 == -1 or a[i] > a[max_index1]:
            max_index1 = i

    max_index2 = -1
    for j in range(0, n):
        if (j != max_index1) and (max_index2 == -1 or a[j] > a[max_index2]):
            max_index2 = j

    return a[max_index1] * a[max_index2]

n = np.int64(input())
a = [np.int64(x) for x in input().split()]
assert(len(a) == n)

result = max_pairwise_product_fast(n, a)

print(result)

## Stress testing

#while True:

#    n = np.random.randint(2, 1000, 1, dtype="int64")[0]
#    print(n)

#    a = []

#    for _ in range(0, n):
#        a.append(np.random.randint(0, 99999, 1, dtype="int64")[0])

#    for i in range(0, n):
#        print(a[i], end=' ')

#    res1 = mpp.max_pairwise_product_slow(n, a)
#    res2 = mpp.max_pairwise_product_fast(n, a)

#    if res1 != res2:
#        print('\n Wrong Answer. {} and {}\n'.format(res1, res2))
#        break
#    else:
#        print('\nOK\n')

