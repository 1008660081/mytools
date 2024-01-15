from urllib.parse import urlparse
from urllib.parse import urlparse, urlunparse

def process_url_with_params(url):
    # 解析 URL
    parsed_url = urlparse(url)
    # 检查路径是否以斜杠结尾
    if parsed_url.path.endswith('/'):
        # 如果是，去掉最后一个字符
        parsed_url = parsed_url._replace(path=parsed_url.path[:-1])
    # 重新构建 URL
    processed_url = urlunparse(parsed_url)
    return processed_url


def remove_duplicates_by_path(urls):
    unique_urls = []
    seen_paths = set()

    for url in urls:
        parsed_url = urlparse(process_url_with_params(url))
        path_parts = parsed_url.path.rsplit('/', 1)
        base_path = path_parts[0]

        if base_path not in seen_paths:
            seen_paths.add(base_path)
            unique_urls.append(url)

    return unique_urls

# 从文件"a.txt"读取URL列表
with open('a.txt', 'r') as file:
    url_list = [line.strip() for line in file]

# 调用去重函数
unique_urls = remove_duplicates_by_path(url_list)

# 将去重后的URL列表输出到文件"out.txt"
with open('out.1111', 'w') as file:
    for url in unique_urls:
        file.write(url + '\n')
