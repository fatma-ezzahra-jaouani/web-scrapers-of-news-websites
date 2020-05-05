#importing libraries
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

#opening a parser on the news section of the website (french)
base_site='http://www.wepostmag.com/category/news/'
response_base= rq.get(base_site)
if (response_base.status_code != 200):
  print('\nthe french page cannot be opened')
else:
  L_articles=[]
  all_links=[]
  L_titles=[]
  L_categories=[]
  print('\nthe french page was opened successfully')
  soup=bs(response_base.content, 'html.parser')
  #extracting links for more news pages
  url=[]
  for i in range(5):
    page=base_site+'page/'+str(i+1)+'/'
    url.append(page)
  print('\nfrench scraping in progress..')
  for pg in url:
    response_pg=rq.get(str(pg))
    soup_pg=bs(response_pg.content,'html.parser')
    print('\nfrench scraping in progress....')
    #extracting links of articles
    links=[]
    for i in soup_pg.find_all('div', class_='post-title'):
      link=i.find('a').get('href')
      links.append(link)
      all_links.append(link)
    #extracting content from articles
    for i in links:
      response_i=rq.get(str(i))
      soup_i=bs(response_i.content,'html.parser')
      #extracting the content of the article
      ch=''
      for p in soup_i.find('div', class_='post-content entry-content').find_all('p'):
        ch=ch+p.text
      ch=ch.replace('\n','').replace('\xa0','')
      L_articles.append(ch)
      #extracting the title of the article
      L_titles.append(soup_i.find('h1', class_="entry-title").text.replace('\n',''))
      #extracting the category of the article
      cat=''
      for a in soup_i.find('aside', class_='post-category post-detail-category').find_all('a', rel='category tag'):
        cat=cat+ a.text + '/'
      L_categories.append(cat)
  print('\nfrench scraping is done')
  print('\nyou have extracted ',str(len(L_articles)),'french articles')

  #creation of the french dataframe
  d = {'link': all_links,'titles' : L_titles ,'article': L_articles, 'type': L_categories}
  df = pd.DataFrame(data=d)

  #saving the french dataframe
  df.to_csv('wepostmagnews-fr.csv', index=False, encoding='utf-16')

#opening a parser on the news section of the website (arabic)
base_site='http://www.wepostmag.com/ar/category/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1/'
response_base= rq.get(base_site)
if (response_base.status_code != 200):
  print('\nthe arabic page cannot be opened')
else:
  L_articles=[]
  all_links=[]
  L_titles=[]
  L_categories=[]
  print('\nthe arabic page was opened successfully')
  soup=bs(response_base.content, 'html.parser')
  #extracting links for more news pages
  url=[]
  for i in range(5):
    page=base_site+'page/'+str(i+1)+'/'
    url.append(page)
  print('\narabic scraping in progress..')
  for pg in url:
    response_pg=rq.get(str(pg))
    soup_pg=bs(response_pg.content,'html.parser')
    print('\narabic scraping in progress....')
    #extracting links of articles
    links=[]
    for i in soup_pg.find_all('div', class_='post-title'):
      link=i.find('a').get('href')
      links.append(link)
      all_links.append(link)
    #extracting content from articles
    for i in links:
      response_i=rq.get(str(i))
      soup_i=bs(response_i.content,'html.parser')
      #extracting the content of the article
      ch=''
      for p in soup_i.find('div', class_='post-content entry-content').find_all('p'):
        ch=ch+p.text
      ch=ch.replace('\n','').replace('\xa0','')
      L_articles.append(ch)
      #extracting the title of the article
      L_titles.append(soup_i.find('h1', class_="entry-title").text.replace('\n',''))
      #extracting the category of the article
      cat=''
      for a in soup_i.find('aside', class_='post-category post-detail-category').find_all('a', rel='category tag'):
        cat=cat+ a.text + '/'
      L_categories.append(cat)
  print('\narabic scraping is done')
  print('\nyou have extracted ',str(len(L_articles)),'arabic articles')

  #creation of the arabic dataframe
  d = {'link': all_links,'titles' : L_titles ,'article': L_articles, 'type': L_categories}
  df_ar = pd.DataFrame(data=d)

  #saving the arabic dataframe
  df_ar.to_csv('wepostmagnews-ar.csv', index=False, encoding='utf-16')