# Dicts || objects || unordered key:value pairs
# keys must be immutable and unique (int, str, bool)
d = {
    "a": 1,
    "b": [7, 8, 9],
    "c": 3,
    "my_list": [{"a": 1, "b": 2, "here": True}]
}


print(d["c"], d["my_list"][0]["here"])
print(d.get("b"), d.get(1))  # None means not found | undefined

d2 = dict(name="me")
print(d2)
print("in Keys || in Values: ", "name" in d2.keys(), "me" in d2.values())
