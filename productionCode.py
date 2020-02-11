# James Curley
# Sprint 2

import sqlite3
from urllib.request import urlopen
import json
import time
import datetime

# Opens the 5 pages of github jobs
json_1 = urlopen("https://jobs.github.com/positions.json")
json_2 = urlopen('https://jobs.github.com/positions.json?page=2')
json_3 = urlopen('https://jobs.github.com/positions.json?page=3')
json_4 = urlopen('https://jobs.github.com/positions.json?page=4')
json_5 = urlopen('https://jobs.github.com/positions.json?page=5')
# loads GitHub Jobs API positions and loads the json object into a variable
jobs_page1 = json.load(json_1)
jobs_page2 = json.load(json_2)
jobs_page3 = json.load(json_3)
jobs_page4 = json.load(json_4)
jobs_page5 = json.load(json_5)
#Empty list that we will populate with api data
job_list = []
location_list = []
company_list = []
date_list = []

file= open("jobs.txt","w+")

connection = sqlite3.connect('jobs.db')
c = connection.cursor()

def APIDataGrab():
    time.sleep(2)
    for item in jobs_page1:    #loops through page one and writes the data to empty lists
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        file.write("Job Title: " + item["title"] +  " Company: " + item["company"] + " Location: " + item["location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page2:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        file.write("Job Title: " + item["title"] +  " Company: " + item["company"] + " Location: " + item["location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page3:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        file.write("Job Title: " + item["title"] +  " Company: " + item["company"] + " Location: " + item["location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page4:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        file.write("Job Title: " + item["title"] +  " Company: " + item["company"] + " Location: " + item["location"] + " Created at: " + item["created_at"] + "\n")
    for item in jobs_page5:
        job_list.append(item["title"])
        company_list.append(item["company"])
        location_list.append(item["location"])
        date_list.append(item["created_at"])
        file.write("Job Title: " + item["title"] +  " Company: " + item["company"] + " Location: " + item["location"] + " Created at: " + item["created_at"] + "\n")

def data():
    print(job_list)
    print(company_list)
    print(location_list)
    print(date_list)

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS githubJobs(title TEXT, company TEXT, location TEXT, date TEXT)')

def data_entry():
    for i in range(len(job_list)):
        c.execute("INSERT INTO githubJobs (title, company, location, date) VALUES (?, ?, ?, ?)",
                  (job_list[i], company_list[i], location_list[i] , date_list[i]))
        connection.commit()

APIDataGrab()
data()
create_table()
data_entry()
c.close()
connection.close()
file.close()
