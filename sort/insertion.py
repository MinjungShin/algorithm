"""
삽입정렬

인풋 이외에 추가 메모리를 요구하지 않음

현재 데이터의 앞 데이터들과 비교하여
본인보다 큰 데이터 앞, 작은 데이터 뒤에 삽입
"""


def insertion():
    for i in range(1, len(arr)):
        j = i
        # 앞의 데이터가 작아지는 경우가 나타날 때까지
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        print(arr)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    insertion()
    print(arr)
