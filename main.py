import sys
from code_review.core import analyze_code

def main():
    changed_files = sys.argv[1:]
    for file in changed_files:
        with open(file, 'r') as f:
            code = f.read()
            analysis = analyze_code(code)
            print(f"Review for {file}:\n{analysis}")

if __name__ == "__main__":
    main()
