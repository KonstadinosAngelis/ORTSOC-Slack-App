from logging import Logger

from slack_bolt import Ack, Respond

#Helper function: Takes elastic module input (such as zeek/suricata), grabs the latest log of that type, and returns an f-string to output
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
    return (
        f"*{module}* \n"
        f"```Last log seen at {src['@timestamp']}\nDataset: {src['event']['dataset']}"
    )

#Helper function: Takes elastic module input, and returns the average number of logs generated over the last hour
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
        #es = elastic search
        es = context["es"]
        respond(f"{last_log_helper(es, 'zeek')}\nAvg: {avg_logs_per_min(es, 'zeek'):.0f} logs per min over the last hour```\n"
                f"{last_log_helper(es, 'suricata')}\nAvg: {avg_logs_per_min(es, 'suricata'):.0f} logs per min over the last hour```\n") 
    except Exception:
        logger.exception("lastseen failed")
        respond("Couldn't query Elasticsearch, check the app logs.")
