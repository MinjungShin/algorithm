"""
선택정렬

인풋 이외에 추가 메모리를 요구하지 않음

맨 앞에 위치한 값과 최솟값을 교환
맨 앞의 위치를 뺀 나머지 배열에서 계속 반복
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
