# List comprehension
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = [num for num in numbers]
print(new_numbers)

# More list comprehension
numbers = [1, 2, 4, 8, 16, 32]
new_numbers = [num * 2 for num in numbers]
print(new_numbers)

# Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Conditional list comprehension exercise
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names_as_cap = [name.upper() for name in names if len(name) > 5]
print(long_names_as_cap)

# Dictionary comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
