from seleniumwire import webdriver


# 加载驱动
driver = webdriver.Chrome()
# 加载网站
driver.get('https://www.dianping.com/')
cookies = driver.get_cookies()
# print(cookies)
li = []
for cookie in cookies:
    # print(cookie)
    name = cookie['name']
    value = cookie['value']
    li.append(f'{name}={value}')

cookie = '; '.join(li)
print(cookie)
