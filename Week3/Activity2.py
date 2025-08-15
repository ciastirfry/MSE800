# Week 3 - Activity 2: Count Words in a File
# Student: Fredierick Saladas

class WordCounter:
    def __init__(self, filepath):
        self.filepath = filepath

    def count_words(self):
        """Reads the file and returns the total number of words."""
        infile = open(self.filepath, "r", encoding="utf-8")
        text = infile.read()
        infile.close()

        # Split by whitespace to get words
        words = text.split()
        return len(words)


def main():
    src = r"C:\Users\freds\MSE800-2025-2026\Week3\demo.txt"
    counter = WordCounter(src)

    total_words = counter.count_words()
    print("=== Word Count Result ===")
    print(f"Total number of words: {total_words}")


if __name__ == "__main__":
    main()