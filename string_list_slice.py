a = "string"
b = len(a)
print(b)

print(a[0:0])
print(a[1:1])
print(a[2:2])
print(a[3:3])
print(a[4:4])
print(a[5:5])
# If the first number is equal the second number in a slice. Nothing output.

print(a[:0])
# print("string"[:0]) output nothing.

print(a[5:])
# print(a[b - 1:]) will output the last character.

# If the first number in a slice is omitted, it is taken to be the
# start of the list.
# If the second number is omitted, it is taken to be the end.
