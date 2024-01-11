用来去重从时光机获取的数据, 通过参数组合排序然后统计出现次数来去重
忽略掉对路径相关的逻辑判断

用法:
python3 waybackurlless.py | tee outputs/output.txt

python3 waybackurlless.py | unfurl format %p?%q | tee outputs/output.txt
