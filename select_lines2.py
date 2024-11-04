import sys
import gzip

def read_patterns(pattern_file):
    with open(pattern_file, 'r') as f:
        patterns = {line.strip() for line in f if line.strip()}
    return patterns
def filter_lines(data_file, patterns):
    with gzip.open(data_file, 'rt') as f:
        for line in f:
            if line.startswith("transcript_id(s)"):
                yield line.strip()
                continue
            line = line.strip()
            columns = line.split('\t')
            for pattern in patterns:
                if any(pattern in col for col in columns):
                    yield line
                    break  # Exit the loop after yielding the line
def main(pattern_file, data_file):
    patterns = read_patterns(pattern_file)
    for matching_line in filter_lines(data_file, patterns):
        print(matching_line)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python select_lines2.py <pattern_file> <data_file>")
        sys.exit(1)

    pattern_file = sys.argv[1]
    data_file = sys.argv[2]
    main(pattern_file, data_file)


