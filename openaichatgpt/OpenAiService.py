import os
import sys
from openaichatgpt.OpenAiGateway import OpenAiGateWay

CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)


class OpenAiService:
    def __init__(self, OpenAiGateway=OpenAiGateWay()):
        self.OpenAiGateway = OpenAiGateway

    def ask(self, query):
        requestData = ('{'
                       '"model": "gpt-3.5-turbo",'
                       '"messages": [{"role": "user", "content": "' + query + '"}],'
                       '"temperature": 0.7'
                       '}'
                       )

        response = self.OpenAiGateway.completion(requestData)

        return response
