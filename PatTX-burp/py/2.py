def remove_prefix(line, prefix):
    if line.startswith(prefix):
        return line[len(prefix):]
    else:
        return line

def process_file(input_file, output_file, prefix):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            processed_line = remove_prefix(line.strip(), prefix)
            outfile.write(processed_line + '\n')

if __name__ == "__main__":
    input_file_path = "out.log"  # 替换为你的输入文件路径
    output_file_path = "out.txt"  # 替换为你的输出文件路径
    prefix_to_remove = "https://www.amazon.com/"

    process_file(input_file_path, output_file_path, prefix_to_remove)

