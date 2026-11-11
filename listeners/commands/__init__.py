from slack_bolt import App

from .es_health import es_health
from .es_event_count import es_event_count

def register(app: App):
    app.command("/es_health")(es_health)
    app.command("/es_event_count")(es_event_count)
