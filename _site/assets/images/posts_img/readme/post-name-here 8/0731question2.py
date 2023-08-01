# 1
numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8]
unique_numbers = []

# 중복을 제거하기 위한 for in 문 사용
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)


# 2
fruits = ["apple", "banana", "orange", "apple", "grape", "banana"]
unique_fruits = []

# 중복을 제거하기 위한 for in 문 사용
for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

print(unique_fruits)

# 3
bool_values = [True, False, True, True, False]
unique_values = []

# 중복을 제거하기 위한 for in 문 사용
for value in bool_values:
    if value not in unique_values:
        unique_values.append(value)

print(unique_values)

# 4
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 22},
]
unique_students = []

# 중복을 제거하기 위한 for in 문 사용
for student in students:
    if student not in unique_students:
        unique_students.append(student)

print(unique_students)

# 5
mixed_data = [1, "apple", True, "banana", 1, 2, True, "orange", 3]
unique_data = []

# 중복을 제거하기 위한 for in 문 사용
for data in mixed_data:
    if data not in unique_data:
        unique_data.append(data)

print(unique_data)
