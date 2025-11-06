def filter_and_square(nums:list[int]) -> list[int]:
    multiplication_data = []
    for n in nums:
        if n>3 and n%2 ==0:
            multiplication_data.append(n*n)
    return multiplication_data

def filter_and_square2(nums: list[int]) -> list[int]:
    return [
        n ** 2
        for n in nums
        if n % 2 == 0 and n > 3
    ]

print(filter_and_square([1, 2, 3, 4, 5, 6, 7]))
print(filter_and_square2([1, 2, 3, 4, 5, 6, 7]))