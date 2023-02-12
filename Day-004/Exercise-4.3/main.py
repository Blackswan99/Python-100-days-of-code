# Don't change the code below
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above

#Write your code below this row

input_y = position[0]
input_x = position[2]
if input_x == "1":
    row1[int(input_y)-1] = "X"
elif input_x == "2":
    row2[int(input_y)-1] = "X"
elif input_x == "3":
    row3[int(input_y)-1] = "X"
else:
    print("Wrong input")

#Write your code above this row

# Don't change the code below
print(f"{row1}\n{row2}\n{row3}")

