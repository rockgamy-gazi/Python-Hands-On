# Square Numbers with Comprehensions and Generators

# 1. Using a list comprehension
squares_list = [x**2 for x in range(1, 21)]
print("Squares using list comprehension:")
print(squares_list)

# 2. Using a generator expression
squares_gen = (x**2 for x in range(1, 21))
print("\nSquares using generator expression:")
for value in squares_gen:
    print(value, end=" ")
