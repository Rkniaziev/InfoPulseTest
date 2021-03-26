s="Long sentence with spaces and dots..."
s=s.split(" ")
print(s)

print(s[-3])

print(s[1][0])

print(s[-1][-1])  # Ну тут у меня не буква последняя 
print(s[-1][-4])  # А вот прям что бы буква, то вот так вот 

s.append("the")
print(s)

s.insert(3, "new2")
print(s)

s.pop(0)
print(s)

s.remove("new2")
print(s)
