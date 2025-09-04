def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 ==0:
            even_numbers.append(num)
    return even_numbers

numbers = [2, 4, 6, 8, 8, 3, 5, 56, 345, 54, 77, 89]

result = filter_even_numbers(numbers)

print("Original List", numbers)
print("Even Numbers", result)
