import os
import sys
import argparse


def search_word(line, search_text):
    words = line.split()
    context = []
    for i, word in enumerate(words):
        if search_text in word:
            start = max(0, i - 5)
            end = min(len(words), i + 6)
            context = words[start:end]
            break
    return ' '.join(context)


def read_logs(directory, text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if text in line:
                            context = search_word(line, text)
                            print(f"File: {file_path}\nLine: {i + 1}\nContext: {context}\n" + "-" * 80)


def main(args):
    parser = argparse.ArgumentParser(description="Analyze log files for specific text.")
    parser.add_argument('logs_dir', type=str, help="Directory containing log files.")
    parser.add_argument('--text', type=str, required=True, help="Text to search for in log files.")

    parsed_args = parser.parse_args(args)

    # Получаем абсолютный путь к директории с логами
    logs_dir = os.path.abspath(parsed_args.logs_dir)

    if not os.path.isdir(logs_dir):
        print(f"The directory {logs_dir} does not exist.")
        sys.exit(1)

    read_logs(logs_dir, parsed_args.text)


if __name__ == "__main__":
    main(sys.argv[1:])
