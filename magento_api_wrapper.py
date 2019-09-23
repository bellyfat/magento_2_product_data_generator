import requests as http_request
from requests import Request
import http.client
import constants


# get admin auth token from Magento store using API
def getAuthToken():
    response = http_request.post(
        constants.AUTH_URL, json=constants.CREDENTIALS)
    return response.text.replace('"', '')


# post data to Magento  store using API
def postData(url, json_data, auth_token):

    header = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

    response = http_request.post(
        url, data=json_data, headers=header)
    return response.text
