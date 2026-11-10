import logging
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from elastic_agent import create_es_client
from dotenv import load_dotenv


from listeners import register_listeners
load_dotenv()

logging.basicConfig(level=logging.DEBUG)

# Initialization
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Elasticsearch connection
es = create_es_client()
print("LOOK HERE: ")
es.info()

# Register Listeners
register_listeners(app)

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
