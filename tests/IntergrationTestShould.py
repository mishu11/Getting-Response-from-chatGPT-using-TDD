import flask_unittest
import json
from openaichatgpt.OpenAiController import app


class IntegrationTest(flask_unittest.ClientTestCase):
    app = app

    def test_if_query_can_give_command(self, client):
        '''when queried responds back with command'''

        query = "command to find files that start with xyz"  # arrange

        response = client.get('/ask/' + query)  # act

        response = json.loads(response.text)
        print(response)

        # ask
        assert response["command"] != True
        assert response["info"] != True
