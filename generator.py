# Given one word, predict the next word.

# Sample text: The ones that love us never really leave us.
word_pairs = {
    "The": "ones",
    "ones": "that",
    "that": "love",
    "love": "us",
    "us": "never",
    "never": "really",
    "really": "leave",
    "leave": "us."
}

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
        next_word = word_pairs.get(current_word, "[END]")
        print(next_word, end=" ")

        # Stop if we've reached the end
        if next_word == "[END]":
            break

        current_word = next_word
