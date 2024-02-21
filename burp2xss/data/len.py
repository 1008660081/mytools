def filter_words(line):
    words = line.split()
    filtered_words = [word for word in words if len(word) <= 20]
    return ' '.join(filtered_words)

def process_file(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            filtered_line = filter_words(line)
            if filtered_line:  # 只有当filtered_line不为空时才写入
                output_f.write(filtered_line + '\n')

if __name__ == "__main__":
    input_file_path = 'params.txt'  # 替换为你的输入文件路径
    output_file_path = 'output.txt'  # 替换为你的输出文件路径

    process_file(input_file_path, output_file_path)
