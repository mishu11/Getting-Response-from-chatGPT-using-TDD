import unittest
from openaichatgpt.responseParser import jsonParser


class ResponseTest(unittest.TestCase):
    response = "{\"id\":\"chatcmpl-6wy93Cf3ZNRPAE1u1EJtLfboIcJzr\", \"object\":\"chat.completion\", \"created\":1679512241, \"model\":\"gpt-3.5-turbo-0301\", \"usage\":{\"prompt_tokens\":15, \"completion_tokens\":41, \"total_tokens\":56}, \"choices\":[{\"message\":{\"role\":\"assistant\", \"content\":\"\\nIn Ruby, you can use the following code:\\n\\n```ruby\\nputs \\\"Hello, World!\\\"\\n```\\nThanks for using chatGPT.\"}, \"finish_reason\":\"stop\", \"index\":0}]}\n"

    jsonParserObj = jsonParser()
    jsonParserObj.set_api_response(response)

    jsonParserObj.parse_api_response()

    def test_to_verify_if_content_is_present(self):
        assert "```" in self.jsonParserObj.get_content()

    def test_to_get_command(self):
        assert self.jsonParserObj.get_command().startswith("puts ")

    def test_to_get_info(self):
        assert self.jsonParserObj.get_info().startswith("Thanks for using chatGPT.")
