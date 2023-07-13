


import  requests


if __name__ == '__main__':
    query = input("请输入需要翻译的单词：")


    data={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }


    url = f'https://fanyi.baidu.com/sug'

    dot = {
        "kw": query
    }
    resp = requests.post(url,data=dot)
    print(resp.json())
    print(resp.url)