# Week 3 - Activity 1: File Handling with OOP (print with line[0:-1])
# Student: Fredierick Saladas

class FileProcessor:
    def __init__(self, infile_path, outfile_path):
        self.infile_path = infile_path
        self.outfile_path = outfile_path

    def process_file(self):
        # --- READ ---
        infile = open(self.infile_path, "r", encoding="utf-8")

        print("=== Original Content ===")
        for line in infile:
            print(line[0:-1])  # Print without the last character (newline)

        infile.close()

        # --- COPY CONTENT ---
        infile = open(self.infile_path, "r", encoding="utf-8")
        outfile = open(self.outfile_path, "w", encoding="utf-8")

        for line in infile:
            outfile.write(line)

        infile.close()
        outfile.close()

        print(f"\nCopy written to: {self.outfile_path}")


def main():
    src = r"C:\Users\freds\MSE800-2025-2026\Week3\demo.txt"
    dst = r"C:\Users\freds\MSE800-2025-2026\Week3\demo_copy.txt"

    processor = FileProcessor(src, dst)
    processor.process_file()


if __name__ == "__main__":
    main()
