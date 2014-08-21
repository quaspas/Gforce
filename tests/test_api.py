import unittest
from client.client import Gforce
from localsettings import API_CLIENT_KEY, API_SECRET_KEY


class TestApiCredentials(unittest.TestCase):

    def test_api_secret_key_returns_200_OK(self):
        g = Gforce(API_SECRET_KEY)
        g.curl('GET','/tours')
        expected = 200
        actual = g.curl('GET','/tours').response.status_code
        self.assertEqual(actual, expected)


    def test_api_client_key_returns_200_OK(self):
        g = Gforce(API_CLIENT_KEY)
        g.curl('GET','/tours')
        expected = 200
        actual = g.curl('GET','/tours').response.status_code
        self.assertEqual(actual, expected)

class TestGforceResponseObject(unittest.TestCase):

    pass
