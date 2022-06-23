import requests
import bs4

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '_ga=GA1.2.1619535988.1655110659; _ym_uid=1655110659549352159; _ym_d=1655110659; hl=ru; fl=ru; visited_articles=349860:110731; _gid=GA1.2.1820276559.1655868301; _ym_isad=2; habr_web_home_feed=/all/',
    'Host': 'habr.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'

}

response = requests.get(base_url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all("article")

for article in articles:

    words = article.find_all(class_="article-formatted-body")
    words = [word.text for word in words]
    words_set = set(words)
    n_art = []
    for word in words:
        for i in KEYWORDS:
            for j in words:
                if i in j:
                    n_art.append(j)
        if word in n_art:
            pub_date = article.find(class_='tm-article-snippet__datetime-published').text
            href = article.find(class_="tm-article-snippet__title-link").attrs['href']
            title = article.find("h2").find("span").text
            result = f'{pub_date} - {title} - {base_url}{href}'
            print(result)
