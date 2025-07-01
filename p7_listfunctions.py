lucky_number=[1,5,3,6,0,2]
enemy=["Alok","Anirudh"]
friends=["saraswati","Ankit","Arun","Ashok","Anand","Aroma"]
friends.append("Babita") #add an element to the list
print(friends)
friends.extend(enemy) # merges two lists into one list
print(friends)
friends.insert(1,"kelly") # inserts an element in between the list
print(friends)
friends.remove("Aroma") # removes an element from the list
print(friends)
friends.pop() # pops the last element from the list
print(friends)
print(friends.index("Anand"))  # checks whether the element is present or not in the list
print(friends.count("Ankit")) #counts the number of time element is present in the list
lucky_number.sort()
print(lucky_number) # sorts in ascending order
lucky_number.reverse()
print(lucky_number) #sorts in descending order
friends2=friends.copy() # copies the list as it is
print(friends2)




