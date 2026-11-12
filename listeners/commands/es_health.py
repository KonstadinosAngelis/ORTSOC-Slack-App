from logging import Logger

from slack_bolt import Ack, Respond

def es_health(command, ack: Ack, respond: Respond, logger: Logger, context):
    ack()
    try:
        #es = elastic search
        cluster = context["es"].cluster.health()
        respond(f"Cluster Name: `{cluster['cluster_name']}` | Status: `{cluster['status']}`") 
    except Exception:
        logger.exception("es_health failed")
        respond("Couldn't reach Elasticsearch, check the app logs.")
