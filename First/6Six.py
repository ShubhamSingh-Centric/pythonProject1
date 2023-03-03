num = 121

d1 = {"a": 1221, "b": 2344, "c": 23442, "d": 6544}


print(d1)
print(d1.keys())
print(d1.values())
print(d1.get("a"))
print(d1["a"])

print(d1.items())


print("***"*20)

print(d1.pop("a"))

print(d1)

print(d1.popitem())

print(d1)

print("***"*20)

d2 = d1.copy()
print("d1", d1)
print("d2", d2)

d1.popitem()
print("d1", d1)
print("d2", d2)

d2.clear()
print("d1", d1)
print("d2", d2)

print("***"*20)

d1.update({"a": 1221})
print(d1)

d2.update(d1)
print("d2", d2)

d3 = {**d1, **{"f": 23422}}
print("d3", d3)

d4 = {**d1, **d2}
print("d4", d4)

