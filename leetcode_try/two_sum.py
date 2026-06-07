def twoSum(num_list: list[int], target: int) -> list[int]:
    for i in range(0, len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                return [i, j]


num_list = [2, 7, 11, 15]
target = 9
sol = twoSum(num_list, target)
print(sol)
