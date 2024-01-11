#  12n.py
#一个用于快速把单个参数变成多个参数的脚本
from urllib import request, parse
#f = open("parameters.txt")
#f = open("ta_parameters.txt")
f = open("dell-test-parameters.txt")
line = f.readline()
parameters = []
num = 0
#多少个参数为一组
n = 50

i = 0

while line:
  parameter = line.strip()
  line = f.readline()
  parameters.append(parameter)
f.close()
#xss = "lol0'\"<'lol1\"lol2<lol3\\x"
#xss = parse.quote("<") + "lol"
xss = "lol0"
#xss = "aaaa"

out = ""

for parameter in parameters:
  num = num + 1
  i = i + 1
  #i = ''
  out += parameter + "=" + xss + str(i) + "&"
  if (num == n):
    print(out[:-1])
    out = ""
    num = 0
print(out[:-1])
