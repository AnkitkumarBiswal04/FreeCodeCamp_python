# for loop is used for accessing the elements in an array or string or series of numbers

#for loop in case of series of number
# it prints number from 0 to 9
for index in range(10):
    print(index)

#for loop in case of series of number
# it prints number from 4 to 9
for index in range(3,10):
    print(index)

#for loop in case of array
friends=["ankit","Arun","Ashok"]
for friend in friends:
    print(friend)

#for loop in case of string
for letter in "Ankit Kumar Biswal":
    print(letter)

#length of the array
print(len(friends))

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("no iteration")