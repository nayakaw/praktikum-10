def tukar(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubbleSort(A, n):
    for i in range(n -1):
        if A[i] > A[i + 1]:
            tukar(A, i, i + 1)
        if n - 1 >1:
            bubbleSort(A, n - 1)
        
A = [4, 7, 6, 9, 8, 1, 2]
bubbleSort(A, len(A))
print("list yang sudah disorting")
print(A)