import urllib.parse as urlparse

# 可以调整，数据越大，结果越多
# 举个例子，设置为10，同参数名的不同路径会输出10个
max = 1

f = open("urls.txt")

line = f.readline()
ok = {}
urls = []

while line:
    url = line.strip()
    line = f.readline()
    parsed = urlparse.urlparse(url)
    query = urlparse.parse_qs(parsed.query)
    query = {k: v[0] for k, v in query.items()}
    print (query)
    querylist = list(query)
    querylist.sort();
    print (querylist)
    querystr = "|".join(querylist)
    print (querystr)
    ok[querystr] = ok.get(querystr,0) + 1
    if (ok[querystr] <= max):
        urls.append(url)
    
f.close()


print("结果输出")

for url in urls:
    print(url)