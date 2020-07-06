import pytest
import requests
import json
import jsonpath
from common.requests_supporting_methods import *
global id

def test_post_request():
    requestURL = create_request_url('api/studentsDetails')
    f = open('C:/Users/supriya.parandkar/PycharmProjects/PytestProject/test_data/students_test_data', 'r')
    json_request = json.loads(f.read())
    response = requests.post(requestURL, json_request)
    assert response.status_code == 201
    global id
    id = response.json()['id']


def test_get_student_data():
    requestURL = create_request_url('api/studentsDetails/111')
    response = requests.get(requestURL)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 111

def test_update_student_data():
    global id
    f = open('C:/Users/supriya.parandkar/PycharmProjects/PytestProject/test_data/students_test_data_put', 'r')
    json_request = json.loads(f.read())
    json_request["id"] = id
    requestURL = create_request_url('api/studentsDetails/{}'.format(id))
    response = requests.put(requestURL, json_request)
    json_response = response.json()
    print(json_response)
    assert response.status_code == 200


def test_delete_student_data():
    global id
    requestURL = create_request_url('api/studentsDetails/{}'.format(id))
    response = requests.delete(requestURL)
    json_response = response.json()
    print(json_response)
    assert response.status_code == 200




