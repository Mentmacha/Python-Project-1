#asking user to feed information ,Remove the whitespaces &capitalizing
name=input("What's your name ?").strip().title()

  

print (f"hello,{name}")#formatting my name 
print(name)



  #split users name to get one single name
first,last=name.split(" ")
print (f"hello,{first}")
