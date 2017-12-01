import random


def arr_min(arr):
    mini = arr[0]

    for i in range(1, len(arr) - 1):
        if arr[i] < mini:
            mini = arr[i]
    return mini


def avg(arr):
    summ = 0
    for x in arr:
        summ += x
    summ /= len(arr)
    return summ


def qsort(arr):
    qsort_rec(arr, 0, len(arr) - 1)


def qsort_rec(arr, l, r):
    if l >= r:
        return
    q = partition(arr, l, r);
    qsort_rec(arr, l, q-1);
    qsort_rec(arr, q+1, r);


def partition(arr, l, r):
    rq = random.randint(l, r);
    arr[rq], arr[r] = arr[r], arr[rq]

    q = l

    for u in range(l, r):
        if arr[u] < arr[r]:
            arr[q], arr[u] = arr[u], arr[q]
            q += 1

    arr[r], arr[q] = arr[q], arr[r]

    return q


array = [4, 7, 8, 1, 3, 0, 3, -5, 1];
print(arr_min(array))
print(avg(array))
qsort(array)
print(array)