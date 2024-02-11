import pytest
import json

#first name of the file and the second is the name of the flask api
from app import app

#In Pytest, a fixture is a way to provide setup
# code that will be run before each test function. Fixtures are used 
#to initialize objects, set up resources, or perform any necessary steps 
#that need to be taken before a test runs. Pytest fixtures help in creating
# a clean and consistent environment for testing.



@pytest.fixture
def client():
    #app is the flask application and it has the test_client
    return app.test_client()


def test_ping(client):
    #sending a get request to method ping
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi there, I'm working!"}


def test_predict(client):

    test_data = {"Gender":"Male", "Married":"Unmarried","Credit_History" : "Unclear Debts",
        "ApplicantIncome":100000,"LoanAmount":2000000}
    resp = client.post("/predict", json=test_data)

    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status': 'Rejected'}
    



