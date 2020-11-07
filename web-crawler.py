import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库
from fake_useragent import UserAgent

ua = {"User-Agent": UserAgent().chrome}
ua1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/86.0.4240.111 Safari/537.36"}
print(ua)
print(ua1)
res_foods = requests.get('http://www.xiachufang.com/explore/', headers=ua)
# 获取数据
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# 解析数据
list_foods = bs_foods.find_all('div', class_='info pure-u')
# 查找最小父级标签
# print(list_foods)
for food in list_foods:
    print(food.find('a').text.strip())
    print('http://www.xiachufang.com{}'.format(food.find('a')['href']))
    print(food.find(class_='ing ellipsis').text)
    print(food.find(class_='stats green-font').text)
    print(food.find(class_='author').text)
    print("-------------------------------------------")
