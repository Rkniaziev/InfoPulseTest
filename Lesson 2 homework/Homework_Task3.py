s = "Long sentence with some new worlds and spaces and dots..."
s = s.split(" ")
print(s)

print(s[-3])

print(s[1][0])

print(s[-1][-1])  # Ну тут у меня не буква последняя
print(s[-1][-4])  # А вот прям что бы буква, то вот так вот

s.append("the")
print(s)

# ??? А если список будет длиннее, то 3 будет не серединой. Как вычислить середину, чтобы код работал для любой длины списка?
# Поправил

d = (len(s)) // 2
s.insert(d, "new2")
print(s)

s.pop(0)
print(s)

s.remove("new2")
print(s)
