"""
선택정렬
"""


def selection():
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    selection()
    print(arr)
