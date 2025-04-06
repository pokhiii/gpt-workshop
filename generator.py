import random

# Training data: Sample text that the model will "learn" from
sample_text = "The ones that love us never really leave us."


# Tokenization
words = sample_text.split()

# Model
word_pairs = {}

# Training
for i in range(len(words) - 1):
    key = words[i]
    next_word = words[i + 1]

    if key not in word_pairs:
        word_pairs[key] = []

    word_pairs[key].append(next_word)

print("Learned Word Pairs:", word_pairs)

while True:
    # Ask the user to input a starting word
    current_word = input("\nEnter a starting word (or type 'exit' to quit): ")

    # Exit condition
    if current_word.lower() == "exit":
        print("Goodbye!")
        break

    # Check if the word exists in the dictionary
    if current_word not in word_pairs:
        print("Sorry, this word is not in the dictionary. Try again.")
        continue

    # Generate words dynamically
    for _ in range(15):
        next_words = word_pairs.get(current_word, ["[END]"])

        # Sampling
        next_word = random.choice(next_words)

        print(next_word, end=" ")

        # Stop if we've reached the end
        if next_word == "[END]":
            break

        current_word = next_word
