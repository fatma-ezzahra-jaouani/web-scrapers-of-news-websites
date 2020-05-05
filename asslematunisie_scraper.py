#importing libraries
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

#opening the home page
base_site='https://www.asslematunisie.net/'
reponse_base=rq.get(base_site)
soup_base=bs(reponse_base.content, 'html.parser')

if (reponse_base.status_code != 200):
  print('\nthis page cannot be opened')
else:
  print('\nthe page was opened successfully')
  #extracting links of category pages from home page (the number of categories may change in this website according to local news)
  url=[]
  for i in soup_base.find_all('a', itemprop="url"):
    url.append(i.get('href'))
  L_articles=[]
  all_links=[]
  link=[]
  L_titles=[]
  L_categories=[]
  print('\nscraping in progress..')
  for page in url:
    category=str(page)
    response= rq.get(category)
    soup=bs(response.content, 'html.parser')
    print('\nscraping in progress.....')
    link=[]
    for i in soup.find_all('a', class_='read-more'):
      link.append(i.get('href')) #saving a list of links to the articles contained in this category 
      all_links.append(i.get('href')) #saving all the links for the dataset
    for i in link:
      site=str(i)
      response_i= rq.get(site)
      html=response_i.content
      soup_i=bs(html, 'html.parser')
      title=soup_i.find('h1', class_="post-title entry-title").text
      title=title.replace('\n','')
      cat=soup_i.find('a', rel='tag').text
      ch=soup_i.article.text
      ch=ch.replace('\n','').replace('\xa0','')
      L_articles.append(ch)
      L_titles.append(title)
      L_categories.append(cat)
  print('\nscraping is done')
  print('\nyou have extracted ',str(len(L_articles)),'articles')

  #creation of the dataframe
  d = {'link': all_links,'titles' : L_titles ,'article': L_articles, 'type':L_categories}
  df = pd.DataFrame(data=d)

  #saving the dataframe (used the encoding utf-16 for arabic carachters)
  df.to_csv('asslematunisie.csv', index=False,encoding='UTF-16')


