import requests
from bs4 import BeautifulSoup as bs
import time
# requests mamkes http requests(
print('enter some skill that you are not familiar with')
unfamiliar_skill=input('>')
print(f'filtering out {unfamiliar_skill}')
def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=&cboWorkExp1=0').text
    # print(html_text)
    soup=bs(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate (jobs) :
        published_date=job.find('span',class_='sim-posted').text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write (f'company name: {company_name.strip()} \n')
                    f.write(f'required skills: {skills.strip()} \n')
                    f.write(f"more info: {more_info} \n")
                print (f'file {index} saved ')

if __name__=='__main__':
    while True:
        find_jobs()
        print (f'waiting 600s...')
        time.sleep(600)
