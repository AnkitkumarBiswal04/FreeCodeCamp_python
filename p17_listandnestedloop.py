# 2D list and nested loop
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0]) # from the grif fir [] is row next one [] is for column

# or we can use the nested for loop
for row in number_grid:
    for column in row:
        print(column)
