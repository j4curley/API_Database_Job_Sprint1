#test file
from JamesCurleySprint1 import productionCode


def test_good_data():
    job_list = productionCode.job_list
    assert len(job_list) >= 100

def test_job_name():
    job_list = productionCode.job_list
    assert "Backend PHP Developer" in job_list
