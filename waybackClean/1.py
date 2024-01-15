from urllib.parse import urlparse

def deduplicate_urls_with_limit(input_file, output_file, limit=3):
    url_count = {}
    unique_urls = []

    with open(input_file, 'r') as infile:
        for line in infile:
            url = line.strip()
            path = urlparse(url).path

            # 统计路径出现的次数
            url_count[path] = url_count.get(path, 0) + 1

            # 判断是否超过限制
            if url_count[path] <= limit:
                unique_urls.append(url)

    with open(output_file, 'w') as outfile:
        for unique_url in unique_urls:
            outfile.write(unique_url + '\n')

if __name__ == "__main__":
    input_file = "1.txt"
    output_file = "httpx.txt"
    deduplicate_urls_with_limit(input_file, output_file, limit=3)
