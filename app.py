from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from elastic_agent import create_es_client

import logging
import os

from listeners import register_listeners

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.DEBUG)

# Initialization
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Elasticsearch connection
# Creates an elastic search client from elastic_agent.py
es = create_es_client()

#Injects the elastic search client into the context dictionary so any listener can use it
@app.use
def inject_es(context, logger, next):
    context["es"] = es
    next()

# Register Listeners
register_listeners(app)

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
