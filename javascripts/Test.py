from typing import List, Tuple


def max_one(arr: Tuple[int]) -> int:
    return max(arr)


def insertion_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == '__main__':
    # 示例用法
    original_list = [12, 11, 13, 5, 6]
    sorted_list = insertion_sort(original_list)

    print("原始列表:", original_list)
    print("排序后列表:", sorted_list)

    num_list = ['A', 'C', 'e', 'z', 'r']
    print("Max value:", max_one(num_list))
