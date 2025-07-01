print("1)Ankit kumar\nBiswal") # next line
print("2)Ankit kumar\"Biswal") # print quotation

phrase="Arun Kumar Biswal"
print("3)"+phrase) #print string using varialbe

print("4)"+phrase+" is cool") #concanation of string

#functions to modify the string
print("5)"+phrase.lower()+"string into lower case") #to make string into lower case
print("6)"+phrase.upper()+"string into upper case") #to make string into upper case

#functions to check the string
print("7)",phrase.isupper()) # to check all string is in upper case or not
print("8)",phrase.upper().isupper()) # multiple function

print("9)"+"The length of the string which also includes spaces is :",len(phrase)) #Length of the string
print("10)To get a individual character :",phrase[0]) # to extract individual character
print("11) to find the index",phrase.index("A")) # to find the index from the string
print("12) this is the function to replace",phrase.replace("Ankit","Arun"))
