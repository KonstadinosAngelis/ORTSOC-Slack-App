from slack_bolt import App

from .sample_command import sample_command_callback
from .elasticsearch_status import elasticsearch_status

def register(app: App):
    app.command("/sample-command")(sample_command_callback)
    app.command("/elasticsearch_status")(elasticsearch_status)
