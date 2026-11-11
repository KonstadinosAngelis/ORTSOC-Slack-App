from slack_bolt import App

from .sample_command import sample_command_callback
from .es_health import es_health
from .es_event_count import es_event_count

def register(app: App):
    app.command("/sample-command")(sample_command_callback)
    app.command("/es_health")(es_health)
    app.command("/es_event_count")(es_event_count)
