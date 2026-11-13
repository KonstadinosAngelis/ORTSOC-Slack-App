from logging import Logger

from slack_bolt import Ack, Respond

from datetime import datetime
from zoneinfo import ZoneInfo

PACIFIC = ZoneInfo("America/Los_Angeles")

# Helper function: Takes elastic module input (such as Zeek/Suricata), grabs the latest log of that type, and returns an f-string to output
def last_log_helper(es, module):
    hits = es.search(
        index="logs-*",
        size=1,
        query={"term": {"event.module": module}},
        sort=[{"@timestamp": "desc"}],
    )["hits"]["hits"]

    if not hits:
        return f"*{module}*: no logs found"

    src = hits[0]["_source"]
    seen = datetime.fromisoformat(src["@timestamp"].replace("Z", "+00:00")).astimezone(PACIFIC)
    ingested = datetime.fromisoformat(src['event']['ingested'].replace("Z", "+00:00")).astimezone(PACIFIC)
    return (
            f"*{module}* \n```Last log seen at {seen:%Y-%m-%d %H:%M:%S %Z}\n"
            f"Ingested: {ingested:%Y-%m-%d %H:%M:%S %Z}\n"
            f"Agent: {src['agent']['name']}"
        )


# Helper function: Takes elastic module input, and returns the average number of those logs generated over the last hour
def avg_logs_per_min(es, module):
    count = es.count(
        index="logs-*",
        query={
            "bool": {
                "filter": [
                    {"term": {"event.module": module}},
                    {"range": {"@timestamp": {"gte": "now-1h"}}},
                    ]
                }
            },
        )["count"]
    return count / 60


def es_lastseen(command, ack: Ack, respond: Respond, logger: Logger, context):
    ack()
    try:
        # es = elastic search
        es = context["es"]
        respond(
            f"{last_log_helper(es, 'zeek')}\nAvg: {avg_logs_per_min(es, 'zeek'):.0f} logs per min over the last hour```\n"
            f"{last_log_helper(es, 'suricata')}\nAvg: {avg_logs_per_min(es, 'suricata'):.0f} logs per min over the last hour```\n"
        )
    except Exception:
        logger.exception("lastseen failed")
        respond("Couldn't query Elasticsearch, check the app logs.")
