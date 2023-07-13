import  requests


if __name__ == '__main__':
    query = input("请输入搜索内容")

    data={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }


    url = f'https://www.baidu.com/s?wd={query}'


    resp = requests.get(url,headers=data)
    # print(resp.text)
    print(resp.url)