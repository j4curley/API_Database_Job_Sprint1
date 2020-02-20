#################
# James Curley  #
# Senior Design #
# Sprint 3      #
#################

import sqlite3
from urllib.request import urlopen
import json
import time
import feedparser

# Opens different pages of jobs ~50 each page
json_1 = urlopen("https://jobs.github.com/positions.json")
json_2 = urlopen('https://jobs.github.com/positions.json?page=2')
json_3 = urlopen('https://jobs.github.com/positions.json?page=3')
json_4 = urlopen('https://jobs.github.com/positions.json?page=4')
json_5 = urlopen('https://jobs.github.com/positions.json?page=5')

stackoverflow_feed = feedparser.parse('https://stackoverflow.com/jobs/feed')
print(stackoverflow_feed['feed']['title'])
print(len(stackoverflow_feed['entries']))
print("Title: " + stackoverflow_feed['entries'][0]['title'])
print("Description: " + stackoverflow_feed['entries'][0]['description'])
print("Category: " + stackoverflow_feed['entries'][0]['category'])
print("ID: " + stackoverflow_feed['entries'][0]['id'])
print("Link: " + stackoverflow_feed['entries'][0]['link'])
print("Published: " + stackoverflow_feed['entries'][0]['published'])


# loads GitHub Jobs API
jobs_page1 = json.load(json_1)
jobs_page2 = json.load(json_2)
jobs_page3 = json.load(json_3)
jobs_page4 = json.load(json_4)
jobs_page5 = json.load(json_5)

# Empty list to append jobs to based on dictionary keys
job_list = []
company_list = []
location_list = []

date_list = []

conn = sqlite3.connect('jobs.db')
c = conn.cursor()

conn_stack = sqlite3.connect('StackOverFlowJobs.db')
cstack = conn_stack.cursor()


def jobs():
    time.sleep(2)
    for item in jobs_page1:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        # f.write("Job Title: " + item["title"] + " Company: " + item["company"] + " Location: " + item[
        #     "location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page2:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        # f.write("Job Title: " + item["title"] + " Company: " + item["company"] + " Location: " + item[
        #     "location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page3:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        # f.write("Job Title: " + item["title"] + " Company: " + item["company"] + " Location: " + item[
        #     "location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page4:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        # f.write("Job Title: " + item["title"] + " Company: " + item["company"] + " Location: " + item[
        #     "location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page5:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        # f.write("Job Title: " + item["title"] + " Company: " + item["company"] + " Location: " + item[
        #     "location"] + " Created at: " + item["created_at"] + "\n")


def print_data():
    print(job_list)
    print(company_list)
    print(location_list)
    print(date_list)


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS githubJobs(title TEXT, company TEXT, location TEXT, date TEXT)')

def create_stack_table():
    cstack.execute('CREATE TABLE IF NOT EXISTS StackOverFlowJobs(title TEXT, location TEXT, description TEXT, category TEXT, id REAL, '
                   'link TEXT, published TEXT)')

def stack_table_entry(): #inserts into stack overfloew table
    for i in range(len(stackoverflow_feed['entries'])):
        if "location" in str(stackoverflow_feed['entries'][i]):


            cstack.execute("INSERT INTO StackOverFlowJobs(title, location, description, category, id, link, published) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (stackoverflow_feed['entries'][i]['title'], stackoverflow_feed['entries'][i]['location'],
                            stackoverflow_feed['entries'][i]['description'], stackoverflow_feed['entries'][i]['category'],
                            stackoverflow_feed['entries'][i]['id'], stackoverflow_feed['entries'][i]['link']
                            , stackoverflow_feed['entries'][i]['published']))

            conn_stack.commit()



def dynamic_data_entry():
    for i in range(len(job_list)):
        c.execute("INSERT INTO githubJobs (title, company, location, date) VALUES (?, ?, ?, ?)",
                  (job_list[i], company_list[i], location_list[i], date_list[i]))
        conn.commit()


def read_from_db():
    c.execute('SELECT * FROM githubJobs')
    data = c.fetchall()
    print(data)
    for row in c.fetchall():
        print(row)


def main():
    jobs()
    create_table()
    create_stack_table()
    dynamic_data_entry()
    stack_table_entry()
    read_from_db()
    c.close()
    conn.close()
    cstack.close()
    conn_stack.close()
    print(len(job_list))
    print_data()


main()
