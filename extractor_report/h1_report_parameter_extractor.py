import re
import requests
from urllib.parse import urlparse, parse_qs
import time
import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def extract_params_from_text(text):
    # 使用正则表达式提取URL
    # 使用正则表达式提取URL
   # url_pattern = re.compile(r'https?://\S+')
    url_pattern = re.compile(r'https?://[^\s]+') 
    urls = url_pattern.findall(text)
    # 提取参数名
    param_names_list = []
    
    try:
        for ur1 in urls:
        # 处理可能的异常情况
            try:
                url = ur1.replace("\\u0026", "&")
                parsed_url = urlparse(url)
                query_params = parse_qs(parsed_url.query)
                param_names = query_params.keys()
                param_names_list.extend(param_names)
            except Exception as e:
            # 捕获并处理异常
                print(f"处理 URL 时发生异常: {e}")

    except Exception as outer_exception:
        print(f"外部循环发生异常: {outer_exception}")

    finally:
    # 无论是否发生异常都会执行的代码
        print("处理完成。")
    
    # 将url写入文件
    urls_file_path = "out/urls.txt"
    with open(urls_file_path, "a") as urls_output_file:
        for ur1_name in urls:
            url_name = ur1_name.replace("\\u0026", "&")
            urls_output_file.write(f"{url_name}\n")
        urls_output_file.write(f"==========================================================================================================\n")
        
    # 将参数名写入文件
    params_file_path = "out/params.txt"
    with open(params_file_path, "a") as params_output_file:
        for param_name in param_names_list:
            params_output_file.write(f"{param_name}\n")


def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        # 从文件中读取所有行
        lines = file.readlines()
        # 去除每行末尾的换行符
        urls = [line.strip() for line in lines]
    return urls

def make_requests(urls):
    for url in urls:
        try:
            # 发起GET请求
            response = requests.get(url)
            text = response.json()['vulnerability_information']
            title = response.json()['title']
            print(f"URL: {url}, Status Code: {response.status_code}")
            logging.info(f"URL: {url}, Status Code: {response.status_code}, Vuln Info(chars): {len(text)}")
            

            urls_file_path = "out/urls.txt"
            h1_url = url.replace(".json", "")
            with open(urls_file_path, "a") as urls_output_file:
                urls_output_file.write(f"{h1_url}      {title}\n")         

            extract_params_from_text(text)
        except requests.RequestException as e:
            # 处理请求异常
            logging.info(f"URL: {url}, Status Code: {response.status_code}, Failed to fetch")
        
        time.sleep(1)

    
if __name__ == "__main__":
    file_path = "report.txt"  # h1 报告所在路径
    urls = read_urls_from_file(file_path)
    responses = make_requests(urls)

    