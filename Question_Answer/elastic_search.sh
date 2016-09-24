#!/bin/bash
# ------------------------------------------------------------------
# [Masaya Ogushi] Elastic Search
#
#          library for Unix shell scripts.
#
#          Usage:
#              sh shell/elastic_search.sh [KEYWORD]
#          If you use the container, you use the --link option
#               docker run --link {elasticsearch running continaer id} -it docker_dialogue/dialogue bash
#          Confirm the other ip address
#               docker inspect {your container id} | grep IPAddress
# ------------------------------------------------------------------

# -- Body ---------------------------------------------------------
#  SCRIPT LOGIC GOES HERE
if [ $# -ne 2 ]; then
    echo "$0 [HOST (localhost or IP address or domain)] [KEYWORD]"
    exit 1
fi

QUERY=$1:9200/_all/_search?pretty
DOUBLE_QUOTE="\""
KEYWORD=${DOUBLE_QUOTE}${2}${DOUBLE_QUOTE}
echo $HOST

curl -XGET $QUERY -d'
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "title": {
              "query": '$KEYWORD',
              "boost": 10
            }
          }
        },
        {
          "match": {
            "abstract": '$KEYWORD'
          }
        }
      ]
    }
  }
}'
# -----------------------------------------------------------------