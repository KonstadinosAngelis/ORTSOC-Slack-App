from logging import Logger

from slack_bolt import Ack, Respond

def es_event_count(command, ack: Ack, respond: Respond, logger: Logger, context):
    ack()
    try:
        #es = elastic search
        result = context["es"].count(
            index="logs-*",
            query={"range": {"@timestamp": {"gte": "now-1h"}}},
        )
        respond(f"`{result['count']:,}` log events in the last hour")
    except Exception:
        logger.exception("event_count failed")
        respond("Couldn't query Elasticsearch, check the app logs.")
