set1 = {10, 20, 30}
set2 = {5, 10, 15, 20}

# (a) {30}
print(set1 - set2)

# (b) {5, 15, 30}
print(set1.difference(set2).union(set2.difference(set1)))

# (c) {5, 10, 15, 20, 30}
print(set1.union(set2))

# (d) {10, 20}
print(set1.intersection(set2))