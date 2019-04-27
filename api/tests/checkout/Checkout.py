import sys
import os.path
from robot.libraries.String import String
_here = os.path.dirname(__file__)
string = String()
_here = string.fetch_from_left(_here, "api")
sys.path.insert(0, os.path.abspath(os.path.join(_here)))

from jsonschema import validate
import json
import requests


class Checkout(object):
    def __init__(self, env="qa"):
        self.env = env
        self._response = None

        script_dir = os.path.dirname(os.path.abspath(__file__))

        endpoints_file = os.path.join(script_dir, 'data/endpoints.json')
        payloads_file = os.path.join(script_dir, 'data/payloads.json')
        schema_file = os.path.join(script_dir, 'data/schema.json')

        self.endpoints = json.load(open(endpoints_file))
        self.payloads = json.load(open(payloads_file))
        self.schema = json.load(open(schema_file))

    def a_user_wants_to_place_an_order(self):
        pass

    def a_request_with_correct_payload_was_made(self):
        """
        This can be augmented to support different types of method like GET, PUT, DELETE etc.
        """
        self._response = requests.post(
            url=self.endpoints['endpoint'],
            data=self.payloads['correct_payload']
        )

    def a_request_with_incorrect_payload_was_made(self):
        """
        This can be augmented to support different types of method like GET, PUT, DELETE etc.
        """
        self._response = requests.post(
            url=self.endpoints['endpoint'],
            data=self.payloads['incorrect_payload']
        )

    def response_code_should_be(self, code: int = 200) -> None:
        """
        Assertion of status code happens here
        """
        assert self._response.status_code == code

    def response_code_should_contain_5_in_the_beginning(self):
        """
        Assertion of negative status code happens here
        """
        assert 5 in self._response.status_code

    def response_body_should_contain_key_named(self, contains=None):
        """
        Assertion of response body
        """
        if contains is not None:
            assert contains in self._response.json()
        else:
            raise Exception("Expected data for response body cannot be empty.")

    def response_schema_should_be_correct(self, schema_name=None, status_code=None):
        """
        Validation of the schema happens here
        """
        validate(self._response.json(), self.schema[schema_name][status_code])
