import urllib.parse as urlparse

max = 1

f = open("urls.txt")
line = f.readline()
ok = {}
urls = []

while line:
    url = line.strip()
    line = f.readline()
    parsed = urlparse.urlparse(url)
    #ParseResult(scheme='https', netloc='uber.com', path='', params='', query='a=1', fragment='')
    query = urlparse.parse_qs(parsed.query)
    # {'a': ['1']}
    query = {k: v[0] for k, v in query.items()}
    # {'a': '1'}
    querylist = list(query)
    # ['a']
    querylist.sort();
    querystr = "|".join(querylist)
    ok[querystr] = ok.get(querystr,0) + 1
    if (ok[querystr] <= max):
        urls.append(url)  
f.close()

for url in urls:
    print(url)