# James Curley
#COMP 490 Sprint 1

from urllib.request import urlopen
import json

job_list = []       # empty job list that we will fill up later
file = open("jobs.txt", "w+")

##############################
# Creating json object vars  #
##############################
json_object1 = urlopen("https://jobs.github.com/positions.json")
json_object2 = urlopen('https://jobs.github.com/positions.json?page=2')
json_object3 = urlopen('https://jobs.github.com/positions.json?page=3')
json_object4 = urlopen('https://jobs.github.com/positions.json?page=4')
json_object5 = urlopen('https://jobs.github.com/positions.json?page=5')

##############################
#   Loading in json object   #
###############################
pageOneData = json.load(json_object1)
pageTwoData = json.load(json_object2)
pageThreeData = json.load(json_object3)
pageFourData = json.load(json_object4)
pageFiveData = json.load(json_object5)

def api_jobs(): #this function loops through api

    for item in pageOneData:
        #print(item['title'])
        job_list.append(item["title"])
        file.write(item["title"] + "\n")
    for item in pageTwoData:
        #print(item['title'])
        job_list.append(item["title"])
        file.write(item["title"] + "\n")

    for item in pageThreeData:
        #print(item['title'])
        job_list.append(item["title"])
        file.write(item["title"] + "\n")

    for item in pageFourData:
        #print(item['title'])
        job_list.append(item["title"])
        file.write(item["title"] + "\n")

    for item in pageFiveData:
        #print(item['title'])
        job_list.append(item["title"])
        file.write(item["title"] + "\n")

def printJobs():
    print(job_list)

api_jobs()
printJobs()
file.close()
##







