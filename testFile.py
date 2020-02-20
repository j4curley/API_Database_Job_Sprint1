#test file
from JamesCurleySprint1 import productionCode
import pytest
import sqlite3

test_conn = sqlite3.connect('StackOverFlowJobs.db')
test_cursor = test_conn.cursor()

@pytest.fixture
def test_job_info():
    job_list = productionCode.job_list
    assert len(job_list) >= 100

def test_job_title():
    job_list = productionCode.job_list
    assert "Software Engineer" in job_list

def test_jobs_data(fetch_data):
    # any real data should have both full time and Contract
    # jobs in the list, assert this
    data = fetch_data
    full_time_found = False
    contract_found = False
    for item in data:
        if item['type'] == 'Contract':
            contract_found = True
        elif item['type'] == 'Full Time':
            full_time_found = True
    assert  contract_found and full_time_found

def test_database_data():
    test_cursor.execute('SELECT * FROM Jobs')
    data = test_cursor.fetchall()
    assert "location" in test_cursor.fetchall()

def test_save_data():
    # second required test
    demo_data = {'id': 1342, 'type': "Testable"}
    list_data = []
    list_data.append(demo_data)
    file_name = "testStackOverFlow.txt"
    productionCode.save_data(list_data, file_name)
    testfile = open(file_name, 'r')
    saved_data = testfile.readlines()
    #the save puts a newline at the end
    assert f"{str(demo_data)}\n" in saved_data