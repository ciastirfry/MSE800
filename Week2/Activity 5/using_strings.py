# Week 2 - Activity 5: Count the number of words in a sentence using Class

class SentenceProcessor:
    def get_sentence(self):
        """
        Prompt the user to enter a sentence and return it.
        """
        sentence = input("Enter a sentence: ")
        return sentence

    def count_words(self, sentence):
        """
        Count the number of words in the given sentence.
        Words are assumed to be separated by spaces.
        """
        words = sentence.split()
        return len(words)

# Create an object of SentenceProcessor
processor = SentenceProcessor()

# Step 1: Get the sentence from the user
sentence = processor.get_sentence()

# Step 2: Count the number of words
word_count = processor.count_words(sentence)

# Display the result
print(f"The sentence contains {word_count} words.")
