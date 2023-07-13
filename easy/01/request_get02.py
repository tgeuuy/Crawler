import requests

if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"

    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    param = {
        "type": "11",
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 20
    }

    resp = requests.get(url=url, headers=head, params=param)
    print(resp.json())
