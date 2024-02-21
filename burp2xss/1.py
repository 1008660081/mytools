def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line_length = len(line)
                if line_length > 2400:
                    print(f"Line {line_number}: {line_length} characters")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 替换 'your_file.txt' 为你要处理的文件路径
    file_path = 'out.log'
    process_file(file_path)

