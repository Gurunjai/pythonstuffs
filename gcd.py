import numpy as np

def blankinship(nums):
    n = np.size(nums)

    a = np.zeros((n, n+1))
    a[np.arange(0, n), 0] = nums
    a[:, 1:] = np.identity(n)

    while np.count_nonzero(a[:, 0]) > 1:
        first_col = a[:, 0]
        i = np.argmin(np.ma.masked_where(first_col == 0, first_col))

        for j in np.delete(np.arange(0, n), i):
            a[j] -= (a[j, 0] // a[i, 0]) * a[i]
        # print(a)

    i = np.nonzero(a[:, 0])[0]

    gcd = a[i, 0].item(0)

    return gcd

def main():
    li = [108, 24, 120]
    print("GCD value of the list {0} is: {1}".format(li, blankinship(li)))

main()