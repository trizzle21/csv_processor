from random import randint
import json 

from requests import Request, Session

from csv_processor.settings import API_ENDPOINT


class PostmanAPI(object):


    def __init__(self):
        self.set_session()
        self.base_url = API_ENDPOINT
        self.stream = True
        self.verify = True

    def set_session(self):
        self.session = Session()
        self.session.headers.update(self.headers)


    @property
    def headers(self):
        return {
            'Content-Type': 'application/json',
        }


    def build_error(self, url, content, status_code):
        error = ("Error accessing {} because {}, status is {}").format(url, 
                                                                       content, 
                                                                       status_code)
        raise Exception(error)

    def send_request(self, url, method='POST', json=False, data=None):
        url = self.base_url + url
        req = Request(method, url, data=data, headers=self.headers)
        prepped = req.prepare()

        response = self.session.send(prepped,
                                     stream=self.stream,
                                     verify=self.verify
                                    )
        if response.status_code not in [200, 201]:
            self.build_error(url, response.content, response.status_code)
        else:
            return response.content



    def add_collection(self, data):
        url = 'api/json'

        return self.send_request(url, method='POST', json=True, data=json.dumps(compiled_data))
