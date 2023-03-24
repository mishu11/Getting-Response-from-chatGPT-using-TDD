import unittest
from unittest.mock import MagicMock
from openaichatgpt.OpenAiService import OpenAiService


class OpenAiService(unittest.TestCase):
    openai_gateway = MagicMock()
    service_should = OpenAiService(openai_gateway)

    def test_if_service_is_able_to_called_gateway(self):
        query = "command to find files that start with xyz"

        response = self.service_should.ask(query)

        assert self.openai_gateway.completion.iscalled
