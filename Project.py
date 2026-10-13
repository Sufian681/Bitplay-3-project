def find_odd_occurrences(nums: list[int]) -> list[int]:
    if not nums: return []
    xor_sum = 0
    for n in nums: xor_sum ^= n
    rightmost_bit = xor_sum & -xor_sum

    num1, num2 = 0, 0
    for n in nums:
        if n & rightmost_bit: num1 ^= n
        else: num2 ^= n
    return sorted([x for x in (num1, num2) if nums.count(x) % 2 != 0])


print(find_odd_occurrences([4, 3, 4, 5, 5, 2, 3, 3]))  # Output: [2, 3] (2 and 3 occur odd times)
print(find_odd_occurrences([9, 4, 9, 4, 7, 4, 4]))     # Output: [7] (7 occurs odd times)