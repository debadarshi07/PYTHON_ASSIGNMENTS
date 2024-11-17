def remove_Klength_tuples(list_, K):
    return list(filter(lambda tup: len(tup) != K, list_))

list_of_tuples = [(1,2,3), (4,5), (6,7), (8,9,0), (10, 11)]
K = int(input("Enter K: "))
updated_list = remove_Klength_tuples(list_of_tuples, K)
print(f"Remaining tuples: {updated_list}")