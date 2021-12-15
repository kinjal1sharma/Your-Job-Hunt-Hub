import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint

def get_url(post, location):
    template = "https://in.indeed.com/jobs?q={}&l={}"
    url = template.format(post, location)
    return url

def get_record(card,):

    # job url and title

    #job_url = 'https://www.indeed.com' + slide.a.get('href')
    title_tag = card.h2
    job_title = title_tag.find('span').text.strip()
    
    #location and name of company 

    tag = card.find('div', 'company_location')
    company = tag.find('span', 'companyName').text.strip()
    job_location = tag.find('div', 'companyLocation').text.strip()

    #Job summary 
    job_summary = card.find('div', 'job-snippet').text.strip()

    # Post Date and extraction date
    post_date = card.find('span', 'date').text
    
    today = datetime.today().strftime('%Y-%m-%d')
   
   #Job Salary
    try:
        job_salary = card.find('div', 'salary-snippet-container').text.strip()
    except AttributeError:
        job_salary = ''
    #print(job_salary)
    record = (job_title, company, job_location, post_date, today, job_summary, job_salary)
    return record

def main(post, location):
    records = []
    url = get_url(post, location)

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        slide = soup.find('div', 'mosaic-provider-jobcards')
        cards = slide.find_all('div', 'job_seen_beacon')

        for card in cards:
            record = get_record(card)
            records.append(record)
        try:
            url = 'https://in.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break

    with open('indeed.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title', 'Company Name', 'Location', 'Post date', 'Today','Summary', 'Salary'])
        writer.writerows(records)




