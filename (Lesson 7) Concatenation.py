#Concatenation
Name1= "Clement"
Name2="Macharia"
Fullname=Name1+ " "+Name2
Fullname+="!!!!!"
print(Fullname)

#casting a number to a string
decade=str(1980)
print(type(decade))
print(decade)

Statement = "I like rock music from the" + decade + "s"
print(Statement)

#Multiple lines
multiline='''
Hey, how are you?

I was just checking in. 

                                All good?


'''
print(multiline)

#Escaping special characters
sentence='I\'m back at work!\tHey!\n\nwhere\'s this at\\located?\n'
print(sentence)

#String Methods
# print(Name1)
# print(Name1.lower())#Small letters
# print(Name1.upper())#Capital letters

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline+=" "
# multiline= "          "+multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))

# print(len(multiline.rstrip()))

#Build a menu
title="menu".upper()
print(title.center(20, "="))
print("")
print("Coffee".ljust(16, ".") +"$1".rjust(1))
print("cake".ljust(16, ".") +"$2".rjust(1))
print("chapati".ljust(16, ".") +"$3".rjust(1))
print("Bugger".ljust(16, ".") +"$4".rjust(1))






 


   
