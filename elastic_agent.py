import os
from elasticsearch import Elasticsearch

#Initializes an elastic search client that gets passed to all listeners through app.py
def create_es_client() -> Elasticsearch:
    return Elasticsearch(
        os.environ["ELASTICSEARCH_URL"],
        api_key=os.environ["ELASTICSEARCH_API_KEY"],
        request_timeout=10,
    )
