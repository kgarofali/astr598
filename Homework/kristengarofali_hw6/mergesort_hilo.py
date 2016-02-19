def merge_sort_hilo(a):

    global aux
    aux = [0] * len(a)
    sort(a,0,len(a)-1)

def sort(a, lo, hi):

    if hi <= lo:
        return

    mid = lo + (hi-lo)/2
    sort(a,lo,mid)
    sort(a,mid+1,hi)
    merge(a,lo,mid,hi)

def merge(a, lo, mid, hi):

    i = lo
    j = mid + 1
    aux = a[:]

    k = lo
    while k <= hi:
        while ((i<=mid) & (j<=hi)):
            if aux[j] < aux[i]:
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1
            k += 1
        while i<= mid:
            a[k] = aux[i]
            i += 1
            k += 1
        while j <= hi:
            a[k] = aux[j]
            j += 1
            k += 1
