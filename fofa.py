#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import base64
import re
import requests
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', help='xxxxx', dest="query")
    args = parser.parse_args()

    s = args.query

#    print (s)
    encodestr = base64.b64encode(s.encode('utf-8'))
    s1 = str(encodestr, 'utf-8')
    api = "https://fofa.info/api/v1/search/all?email=501674633@qq.com&key=64ad5f6e2a6e3c9c7ca3e1f2f3f6232e&qbase64=%s&size=10000" % s1
#   print (api)

    response = requests.get(api)
 #   print(response.text)

    res = json.loads((response.content).decode('utf-8'))
#   print (res["error"])
#   print (res["size"])


    if res["error"] == "False":
        print("error in query :  " + s)
        return
    else :
        if res["size"] >= 100000000000000000000:
            print (s + "  result more than 1000000")
        else:
            resulits = res["results"]
            for i in resulits:
                print (i[0])


if __name__=='__main__':
    main()

