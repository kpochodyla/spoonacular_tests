from apiKey import Key
import json
import requests


class SpoonacularTests:

    def get_reques_data(self, test_name):
        test_params_file = open('parameters/test_parameters.json')
        tests_data = json.load(test_params_file)
        test_data = tests_data[test_name]
        return test_data['baseUrl'], test_data['parameters']
        
    def get_request_url(self, base_url, request_parameters):
        request_url = base_url
        for data, value in request_parameters.items():
            request_url += '{0}={1}&'.format(data, value)
        return request_url + 'apiKey={0}'.format(Key)

    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
        }

        return headers

    def get_reply(self, base_url, headers=None):
        if (headers == None):
            headers = self.get_headers()
        return requests.get(base_url, headers)