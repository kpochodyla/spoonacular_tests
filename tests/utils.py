from apiKey import Key
import pytest
import json
import requests

class SpoonacularTests:

    def get_request_data(self, test_name):
        test_params_file = open('parameters/test_parameters.json')
        tests_data = json.load(test_params_file)
        request_params = tests_data[test_name]
        return request_params['baseUrl'], request_params['parameters']
        
    def get_request_url(self, base_url, request_parameters):
        request_url = base_url + '?apiKey={0}'.format(Key)
        request_url = request_url.format(**request_parameters)
        for data, value in request_parameters.items():
            request_url += '&{0}={1}'.format(data, value)
        return request_url

    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
        }
        return headers

    def get_request(self, base_url, headers=None):
        if (headers == None):
            headers = self.get_headers()
        return requests.get(base_url, headers)
