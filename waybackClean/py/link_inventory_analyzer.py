from urllib.parse import urlparse
from collections import defaultdict

# 读取文件
file_path = 'urls.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# 使用 defaultdict 统计每个域名下的URL数量
domain_url_count = defaultdict(int)

for line in lines:
    # 提取域名
    url = line.strip()
    domain = urlparse(url).netloc

    # 统计数量
    domain_url_count[domain] += 1

# 对域名进行排序
sorted_domains = sorted(domain_url_count.items(), key=lambda x: x[1], reverse=True)

# 打印排序后的结果
for domain, count in sorted_domains:
    print(f'{domain}: {count} 个URL')

