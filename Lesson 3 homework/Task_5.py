s = "We are not what we should be! \nWe are not what we need to be. \nBut at least we are not what we used to be \n(Football Coach)"
print(s)

count = 0
for i in range(len(s)):
    if s[i] == " ":
        count += 1

print(count + 1)

# Тут я вообще не понимаю как через strip сделать....
b = ""
for i in range(len(s)):
    if s[i] == " ":
        b += ""
    elif s[i] == "!":
        b += ""
    elif s[i] == ".":
        b += ""
    else:
        b += s[i]
print(b)

# Ну или я все же смог сюда strip втулить
a = s.split()
b = ""
for item in a:
    b += item.strip(" !.")
print(b)


p = s.lower()
print(p)
n = p.split()
n.sort()
print(n)


