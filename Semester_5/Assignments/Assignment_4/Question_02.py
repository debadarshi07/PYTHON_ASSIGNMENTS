def rotate (idx1, idx2, idx3):
    return idx3, idx1, idx2

a, b, c = 'Doug', 22, 1984

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)

a, b, c = rotate(a, b, c)
print(a, b, c)