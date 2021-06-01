import unittest

import azure.functions as func
from cooldown import main

class TestFunction(unittest.TestCase):
    def test_CoolDownBlob(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/cooldown',
            params={'path': '/raw/test'})

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertEqual(
        #    resp.get_body(),
        #    b'21 * 2 = 42',
            True
        )