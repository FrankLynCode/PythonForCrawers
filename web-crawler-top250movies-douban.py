#what I do in this program is
#就是把豆瓣TOP250里面的 序号/电影名/评分/推荐语/链接 #都爬取下来，结果就是全部展示打印出来
import requests,bs4,time

movie_rank=list()
for page in range(10):
	url='https://movie.douban.com/top250?start='+str(page*25)+'&filter='
	# url='https://movie.douban.com/top250?start=100&filter='
	# print(url)
	html=bs4.BeautifulSoup(requests.get(url).text,'html.parser')
	# print(html)
	all_info=html.find_all('div',class_='item')
	# print(all_info)
	for movie_info in all_info:
		movie_NO=movie_info.find('em').text
		movie_name= movie_info.find(class_='info').find('a').text
		movie_star=movie_info.find('span',class_='rating_num').text
		if movie_info.find('p',class_='quote') is not None:
			movie_quote= movie_info.find('p',class_='quote').text
		else:
			movie_quote='No comment'
		movie_url=movie_info.find('a')['href']
		movies=list()
		movies.append(movie_NO)
		movies.append(movie_name)
		movies.append(movie_star)
		movies.append(movie_quote)
		movies.append(movie_url)
		movie_rank.append(movies)

for movie in movie_rank:

	print('''
		The NO.{} Movie is :{}
		Rating:{}
		Quote:{}
		Link:{}
		'''.format(*movie))
	time.sleep(2)
