from logging import Logger

from slack_bolt import Ack, Respond


def elasticsearch_status(command, ack: Ack, respond: Respond, logger: Logger):
    try:
        ack()
        respond(f"testing commands")
    except Exception:
        logger.exception("Error responding to elasticsearch_status command")

