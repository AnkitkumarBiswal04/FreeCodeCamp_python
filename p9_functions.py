# we are going to create a function that is going to say hi to the users

#defining the function
def say_hi(number,name,age): #inside the brackets are the parameters
    print("hello user "+number+" : "+name+" is "+str(age)+" years old")

#calling the functionS
print("Top")
say_hi("1","Ankit",24) # note we can pass integer but we need to make integer as string
say_hi("2","Arun",56)
print("bottom")