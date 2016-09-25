import logging
import subprocess
import json
import random

"""
Reference:
    http://www.yamamanx.com/slack-bot-aws-lambda-python-api-gateway/
"""

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def make_query(keyword):
    """
    Make a Elasticsearch search query
    :param keyword(string): set the search key words
    :return (string): elasticsearch search query
    """
    # Simple Query
    query = "curl -XGET 52.69.244.7:9200/_all/_search?pretty -d\'"
    make_query_before = '{ "query": { "match" : { "title": { "query": '
    query_keyword = "\"" + keyword + "\""
    make_query_after = "} } } }\'"
    elasticsearch_query = query + make_query_before + query_keyword + make_query_after
    return elasticsearch_query

def return_code(text):
    """
    Make return code for slack
    :param text(string): slack return text
    :return (string): json format for slack
    """
    payload={'text': text}
    return payload

def lambda_handler(event, context):
    """
    Get the Slack command (using the outgoing) and return the search result
    :param event:
    :param context:
    :return (json): if the exists the image data in the search key, return the image, if the no exist the image, r
                    eturn the wiki url link
    """
    command_text = event['text'].replace("bot_lambda_out ", "")

    elasticsearch_query = make_query(command_text)
    sysmte_output = subprocess.Popen(elasticsearch_query, shell=True, stdout=subprocess.PIPE).stdout.read()
    json_data = json.loads(sysmte_output)
    if json_data['hits']['hits']:
        title = json_data['hits']['hits'][0]['_source']['title']
        abstract = json_data['hits']['hits'][0]['_source']['abstract']
        url = json_data['hits']['hits'][0]['_source']['url']
        image = json_data['hits']['hits'][0]['_source']['image']
        return_data = title + "\n" + abstract + "\n" + url + "\n"
    else:
        return return_code("No match")

    image_list = []
    for hit_data in json_data['hits']['hits']:
        if hit_data['_source']['image']:
            image_list.append(hit_data['_source']['image'])

    if image_list:
        return return_code(return_data + random.choice(image_list))

    if json_data['hits']['hits']:
        return return_code(return_data)