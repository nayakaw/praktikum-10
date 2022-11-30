def findlst(arr, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return findlst(arr, k, low, mid-1)
        else:
            return findlst(arr, k, mid + 1, high)
    else:
        return -1


num = [8,7,3,4,6]
k = int(input("Masukkan angka yang dicari: "))
num.sort()
print("Sesudah di Sorting:",num)
result = findlst(num, k, 0, len(num)-1) + 1

if k in num:
    print("Elemen ditemukan pada posisi ke-" + str(result))
elif k not in num:
    print("Elemen tidak ditemukan")