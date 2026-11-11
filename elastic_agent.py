# elastic_client.py
import os
from elasticsearch import Elasticsearch

def create_es_client() -> Elasticsearch:
    return Elasticsearch(
        os.environ["ELASTICSEARCH_URL"],
        api_key=os.environ["ELASTICSEARCH_API_KEY"],
        request_timeout=10,
    )
