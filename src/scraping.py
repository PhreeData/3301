site = 'https://www.inovacaotecnologica.com.br/boletim/rss.xml'

def hackernews_rss(feedRss):
  article_list = []
  try:
    r = requests.get(feedRss)
    soup = BeautifulSoup(r.content, features='xml')
    articles = soup.findAll('item')        
    for a in articles:
        title = a.find('title').text
        link = a.find('link').text
        published = a.find('pubDate').text
        article = {
            'title': title,
            'link': link,
            'published': published
            }
        article_list.append(article)
    return print(article_list)
  except Exception as e:
      print('The scraping job failed. See exception: ')
      print(e)
print('Starting scraping')
hackernews_rss(site)
print('Finished scraping')