"""
CP1404 Practical
word_occurrences
Code that count word occurrences in a string
"""


text = input("Enter a string: ")
words = text.split()  # Split the input string into words
word_to_count = {}  # Dictionary to store word counts

# Count occurrences of each word
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

# Find the longest word length for alignment
max_word_length = max(len(word) for word in word_to_count.keys())

# Sort and print the results with aligned columns
for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_word_length}} : {count}")


