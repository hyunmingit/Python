"""
날짜 2022.02.18
이름 장현민
내용 삽입정렬 실습
"""

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        #피봇보다 큰 데이터를 찾을 때 까지 반복

        while left <= end and arr[pivot] >= arr[left]:
            left += 1

        #피봇보다 작은 데이터를 찾을 때 까지 반복
        while right > start and arr[pivot] <= arr[right]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)

















