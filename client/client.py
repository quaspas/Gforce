import json
import collections
from requests.models import Request
from requests.sessions import Session


class GforceResponse(collections.Sequence):

    def __init__(self, response):
        self.response = response
        content = response.content.decode('utf-8')
        content = json.loads(content)
        self.count = content.get('count')
        self.page = content.get('page')
        self.results = content.get('results')

    def __len__(self):
        return len(self.results)

    def __getitem__(self, index):
        return self.results[index]


class Gforce(object):

    # curl -H "X-Application-Key: YOUR_APPLICATION_KEY"
    # https://rest.gadventures.com/tours/21346

    SCHEME = 'https'
    HOST = 'rest.gadventures.com'

    def __init__(self, key):
        self.KEY = key

    def curl(self, method, endpoint, params=None):
        url = '{scheme}://{host}{endpoint}'.format(scheme=self.SCHEME, host=self.HOST, endpoint=endpoint)
        params = params or {}
        session = Session()
        request = Request(method, url, params=params)
        request = request.prepare()
        request.headers.update({
            'X-Application-Key': self.KEY,
        })
        response = session.send(request)
        return GforceResponse(response)