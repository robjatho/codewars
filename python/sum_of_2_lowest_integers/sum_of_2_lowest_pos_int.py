def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([5, 8, 12, 19, 22, 27]))
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))