# if statement follows a set of conditions

#simple if statement
is_male=True
if is_male:
    print("you are a male")
else:
    print("you are not a male")


#complex if statement
is_male=True
is_tall=False
if is_male and is_tall:
    print("you are a male")
elif is_male and not(is_tall):
    print("you are short male")
elif not(is_male) and is_tall:
    print("you are not male but tall")
else:
    print("you are not male and not tall")


# if statement and comparasion(>,<,=,>=,<=,!=)
def compare(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    else:
        return num3

num1=input("enter num1 value:")
num2=input("enter num2 value:")
num3=input("enter num3 value:")
result=compare(num1,num2,num3)
print("the largest among three variables is :"+result)
