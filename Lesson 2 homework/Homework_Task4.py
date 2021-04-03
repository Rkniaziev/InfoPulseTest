d = {'Title': 'Americano', 'Price': 11, 'Ingredients': ['espresso', 'water']}
print(d)

d.update(description='Great drink to cheer up!')
print(d)

b=d.get("Price")+100
d.update(Price=b)
print(d)

c=d.get("Ingredients")
c.insert(2,"milk")
print(d)

c=d.get("Ingredients")
print(len(c))

d.pop("description")
print(d)
