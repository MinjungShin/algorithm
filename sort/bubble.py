"""
버블 정렬

인접한 두 원소를 비교하여 크기가 순서대로 되어 있지 않으면 교환
1회전을 수행하고 나면 가장 큰 자료가 맨 뒤로 이동하기 때문에
2회전에서는 맨 끝에 있는 자료 제외
수행할 때마다 정렬에서 제외되는 데이터가 하나씩 늘어남
"""


def bubble():
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    bubble()
    print(arr)
