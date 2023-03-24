from flask import Flask
import os
import sys
from openaichatgpt.OpenAiService import OpenAiService


CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)

app = Flask(__name__)


@app.route('/ask/<query>')
def ask(query, service=OpenAiService()):

    return service.ask(query)


if __name__ == "__main__":
    app.run()
