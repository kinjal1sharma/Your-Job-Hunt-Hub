import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def get_url(post, location):
    original_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={}&txtLocation={}'
    post = post.replace(' ', '+')
    url = original_url.format(post, location)
    url += '&sequence={}'
    return url


def extract_listings(job):

    #company name and url

    job_tag = job.h3
    company_name = job_tag.text.strip()
    a_tag = job.h2.a
    url = a_tag.get('href')

    # location

    job_location_tag = job.find('ul', class_='top-jd-dtl clearfix')
    job_location = job_location_tag.find('span').get('title')


    # post date and today's date

    post_date = job.find('span', class_='sim-posted').text.strip()
    today = datetime.today().strftime('%Y-%m-%d')

    result = (company_name, job_location, post_date, today, url)

    return result

def final(post, location):


    job_listings = []
    url = get_url(post, location)

    for sequence in range(1, 34):
        response = requests.get(url.format(sequence))
        soup = BeautifulSoup(response.text, 'html5lib')
        results = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        for job in results:
            result = extract_listings(job)
            job_listings.append(result)

    # The csv file
    with open('times.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'Job Location', 'Post date', 'Today', 'Url'])
        writer.writerows(job_listings)