file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
f1 = [int(num.strip()) for num in file1]
f2 = [int(num.strip()) for num in file2]
result = [num for num in f1 if num in f2]
# Write your code above

print(result)
