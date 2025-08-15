# Week 3 - Activity 1: File Handling
# Student: Fredierick Saladas

class FileProcessor:
    def __init__(self, infile_path, outfile_path):
        self.infile_path = infile_path
        self.outfile_path = outfile_path

    def process_file(self):
        # --- READ ---
        infile = open(self.infile_path, "r", encoding="utf-8")

        lines_list = []
        for line in infile:
            data = line.rstrip("\n")          # like splitting/stripping per line
            lines_list.append(data)

        print("=== Original Content ===")
        for content in lines_list:
            print(content)

        infile.close()

        # --- WRITE ---
        outfile = open(self.outfile_path, "w", encoding="utf-8")
        for content in lines_list:
            outfile.write(content + "\n")     # write back (could modify if needed)
        outfile.close()

        print(f"\nCopy written to: {self.outfile_path}")


def main():
    src = r"C:\Users\freds\MSE800-2025-2026\Week3\demo.txt"
    dst = r"C:\Users\freds\MSE800-2025-2026\Week3\demo_copy.txt"

    processor = FileProcessor(src, dst)
    processor.process_file()


if __name__ == "__main__":
    main()