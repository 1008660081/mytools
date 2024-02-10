from urllib import request, parse

# 读取文件中的参数
with open("params.txt") as f:
    parameters = [line.strip() for line in f]

# 每组参数的数量
n = 50

# XSS payload
xss = "1z%27z%22z%3cz%2fz123%5cx"

out = ""

for num, parameter in enumerate(parameters, start=1):
    current_num = (num - 1) % n + 1  # 将 num 的范围调整为 1 到 n
    out += f"{parameter}={xss}{current_num}&"
    if num % n == 0:
        print(out[:-1])
        out = ""

# 打印剩余的参数
if out:
    print(out[:-1])
