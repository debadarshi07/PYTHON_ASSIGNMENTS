def unique_pairs(words):
    result = set()

    words = [word for word in words if len(word) >= 4]

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]

            if not set(word1) & set(word2):
                result.add(tuple(sorted((word1, word2))))

    # result = [tuple(sorted((words[i], words[j]))) for i in range(len(words)) for j in range(i + 1, len(words)) if not set(words[i]) & set(words[j])]
    
    return result

words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))