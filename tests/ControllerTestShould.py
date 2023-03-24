import unittest
from unittest.mock import MagicMock
from openaichatgpt.OpenAiController import ask


class ResponseControllerShould(unittest.TestCase):
    service = MagicMock()

    def test_if_contoller_is_able_to_call_the_service(self):
        query = "command to find files that start with xyz"

        response = ask(query=query, service=self.service)

        assert self.service.ask.iscalled
