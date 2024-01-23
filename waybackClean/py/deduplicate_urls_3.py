from urllib.parse import urlparse
from collections import defaultdict

# 读取文件
file_path = 'urls.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# 使用 defaultdict 统计每个域名下的URL数量
domain_url_count = defaultdict(list)

for line in lines:
    # 提取域名
    url = line.strip()
    domain = urlparse(url).netloc

    # 检查域名下的URL数量是否超过500个
    if len(domain_url_count[domain]) < 50:
        domain_url_count[domain].append(url)

# 输出结果到2.txt文件
output_file_path = 'shuf.txt'
with open(output_file_path, 'w') as output_file:
    for domain, urls in domain_url_count.items():
        for url in urls:
            output_file.write(f'{url}\n')

print(f'结果已保存到 {output_file_path}')

