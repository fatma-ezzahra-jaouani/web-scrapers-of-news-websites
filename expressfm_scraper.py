#importing libraries
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

#opening the french actualities section of the website
base_site='https://www.radioexpressfm.com/actualites/'
response_base= rq.get(base_site)

#scraping french news
if (response_base.status_code!=200):
  print('the french page cannot be opened')
else:
  print('page opened successfully')
  soup=bs(response_base.content,'html.parser')
  #getting more pages
  url=[]
  for i in range(4):
    url.append(base_site+'page/'+str(i+1)+'/')
  print('scraping in process..')
  L_titles=[]
  all_links=[]
  L_articles=[]
  L_categories=[]
  for pg in url:
    response_pg=rq.get(str(pg))
    soup_pg=bs(response_pg.content,'html.parser')
    links=[]
    for item in soup_pg.find_all('a', class_="qt-text-shadow"):
      links.append(item.get('href'))
      all_links.append(item.get('href'))
      L_titles.append(item.text.replace('\n',''))
    print('scraping in process.....')
    for i in links:
      response_i=rq.get(str(i))
      soup_i=bs(response_i.content,'html.parser')
      ch=''
      for p in soup_i.find('div', class_='qt-the-content').find_all('p'):
        ch=ch+p.text
      ch=ch.replace('\n','').replace('\xa0','')
      L_articles.append(ch)
      cat=''
      for a in soup_i.find_all('a', rel='category tag'):
        cat=cat+ ' '+a.text
      L_categories.append(cat)
  print('french scraping done')
  print('you have extracted '+ str(len(L_titles)) + ' french articles')

  #creating the french dataframe
  d = {'link': all_links,'titles' : L_titles ,'article': L_articles ,'type': L_categories}
  df = pd.DataFrame(data=d)

  #saving the french dataframe
  df.to_csv('expressfm-fr.csv', index=False,encoding='UTF-16')

#opening the arabic actualities section of the website
base_site='https://www.radioexpressfm.com/ar/%d8%a7%d9%84%d8%a3%d8%ae%d8%a8%d8%a7%d8%b1/'
response_base= rq.get(base_site)

#scraping arabic news
if (response_base.status_code!=200):
  print('the arabic page cannot be opened')
else:
  print('arabic page opened successfully')
  soup=bs(response_base.content,'html.parser')
  #getting more pages
  url=[]
  for i in range(4):
    url.append(base_site+'page/'+str(i+1)+'/')
  print('scraping in process..')
  L_titles=[]
  all_links=[]
  L_articles=[]
  L_categories=[]
  for pg in url:
    response_pg=rq.get(str(pg))
    soup_pg=bs(response_pg.content,'html.parser')
    links=[]
    for item in soup_pg.find_all('a', class_="qt-text-shadow"):
      links.append(item.get('href'))
      all_links.append(item.get('href'))
      L_titles.append(item.text.replace('\n',''))
    print('scraping in process.....')
    for i in links:
      response_i=rq.get(str(i))
      soup_i=bs(response_i.content,'html.parser')
      ch=''
      for p in soup_i.find('div', class_='qt-the-content').find_all('p'):
        ch=ch+p.text
      ch=ch.replace('\n','').replace('\xa0','')
      L_articles.append(ch)
      cat=''
      for a in soup_i.find_all('a', rel='category tag'):
        cat=cat+' '+ a.text
      L_categories.append(cat)
  print('arabic scraping done')
  print('you have extracted '+ str(len(L_titles)) + ' arabic articles')

  #creating the arabic dataframe
  d = {'link': all_links,'titles' : L_titles ,'article': L_articles, 'type': L_categories}
  df_ar = pd.DataFrame(data=d)

  #saving the arabic dataframe
  df_ar.to_csv('expressfm-ar.csv', index=False,encoding='UTF-16')