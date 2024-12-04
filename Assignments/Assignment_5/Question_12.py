sentence = input('Enter a sentence: ')

sentence = ''.join(char for char in sentence if char.isalnum() or char.isspace()).lower()

words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

duplicates = {word: count for word, count in word_count.items() if count > 1}

print(f"There are total {len(duplicates)} words that have been repeated.")
print("Duplicate words and their counts:", duplicates)