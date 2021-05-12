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

def get_record(card):
    #company name and url

    atag = card.h2.a
    job_title = atag.get('title')
    job_url = 'https://in.indeed.com' + atag.get('href')
    company = card.find('span', 'company').text.strip()

    # location

    job_location = card.find('div', 'recJobLoc').get('data-rc-loc')

    # post date and today's date

    post_date = card.find('span', 'date').text
    today = datetime.today().strftime('%Y-%m-%d')
    try:
        job_salary = card.find('span', 'salaryText').text.strip()
    except AttributeError:
        job_salary = ''

    record = (job_title, company, job_location, post_date, today, job_salary, job_url)

    return record

def main(post, location):
    records = []
    url = get_url(post, location)

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all("div", "jobsearch-SerpJobCard")

        for card in cards:
            record = get_record(card)
            records.append(record)
        try:
            url = 'https://in.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break

    with open('indeed.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['JobTitle', 'Company Name', 'Job Location', 'PostDate', 'Extract date', 'Salary', 'Url'])
        writer.writerows(records)


