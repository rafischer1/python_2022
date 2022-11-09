# LISTS || Arrays (basically)
li = [1, 2, 3, 4, True, "a list"]
print(li[2::2])
li[0] = "new item"
print(li[0])

# Matrix (2d lists)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    ["hi", "bye"]
]

print(matrix[2][1])
matrix.reverse()  # modifies in place
new = matrix
print(new)
print([1, 2, 3] in new)

li_two = ["a", "x", "f", "b", "w"]
print(sorted(li_two))

sent = " "
new_sent = sent.join(["hi", "cool"])
print(new_sent)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6]
print(a, c, b, d, other)
