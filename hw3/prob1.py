def bubble_sort(l):
    def swap(i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
    
    n = len(l) - 1
    for i in range(n, 0, -1):
        for j in range(i):
            if (l[j] >= l[j+1]):
                swap(j, j+1)

    return l

def insertion_sort(l):
    n = len(l)

    for j in range(1, n):
        key = l[j]
        i = j - 1
        while((i>=0) and (key < l[i])):
            l[i+1] = l[i]
            i -= 1
        l[i+1] = key
    
    return l

def merge_sort(l):
    def merge(left,right):
        len_left, len_right = len(left), len(right)
        i_left, i_right = 0,0
        l = []

        while((i_left < len_left) and (i_right < len_right)):
            if (left[i_left] < right[i_right]):
                l.append(left[i_left])
                i_left += 1
            else:
                l.append(right[i_right])
                i_right += 1

        while (i_left < len_left):
            l.append(left[i_left])
            i_left += 1
        
        while (i_right < len_right):
            l.append(right[i_right])
            i_right += 1

        return l

    if ((len(l) == 0) or (len(l) == 1)):
            return l
    mid = int(len(l) / 2)

    left = merge_sort(l[0:mid])
    right = merge_sort(l[mid:-1])

    r = merge(left, right)

    return r

def quick_sort(l):
    def partition(l, low, high):
        def swap(i, j):
            t = l[i]
            l[i] = l[j]
            l[j] = t
            return
    
        pivot = l[low]
        mid = low 
        for j in range(low+1, high+1):
            if (l[j] < pivot):
                mid += 1
                swap(j, mid)
        swap(low, mid)
        return mid

    def qs(l, low, high):
        if (low < high):
            pivot_idx = partition(l, low, high)
            qs(l, low, pivot_idx-1)
            qs(l, pivot_idx+1, high)

        return l

    qs(l, 0, len(l) -1)

    return l

def radix_sort(l,d):
    def get_digit(number, d):
        return (number // 10**d) % 10
    
    for m in range(0, d):
        c = [0] * 10
        for i in l:
            key = get_digit(i, m)
            c[key] += 1
        for j in range(1, 10):
            c[j] = c[j-1] + c[j]
        n = len(l)
        t = [0] * n
        for i in range(n-1, -1, -1):
            key = get_digit(l[i], m)
            t[c[key]-1] = l[i]
            c[key] = c[key] - 1
        for i in range(0,n):
            l[i] = t[i]
    return l


