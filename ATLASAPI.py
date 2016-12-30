import requests
import json
import sys


ATLAS_DOMAIN="server1"
ATLAS_PORT="21000"
NAMENODE_PRIMARY="server1.hdp"
NAMENODE_PORT=8020
CLUSTERNAME="HDP"

RANGER_DOMAIN="server1.hdp"
RANGER_PORT="6080"

def atlasREST( restAPI ) :
## TODO Verify received code = 200 or else produce an error
    url = "http://"+ATLAS_DOMAIN+":"+ATLAS_PORT+restAPI
    print "URL request = curl -iv -u admin:admin -X GET %s" % (url)
    r= requests.get(url, auth=("admin", "admin"))
    return(json.loads(r.text));


def atlasPOST( restAPI, postData) :
    url = "http://" + ATLAS_DOMAIN + ":" + ATLAS_PORT + restAPI
    print ("curl -d @entity.json -X POST -H \"Content-Type: application/json\" %s" % (url))
    r = requests.post(url, auth=("admin", "admin"),json=postData)

    jsonResult = {
        "statusCode": r.status_code,
        "msg": r.text,
        "postData" :  postData
    }
    if (r.status_code == 200):
       jsonResult = json.loads(r.text)

    return (jsonResult);
def atlasPUT( restAPI, postData) :
    url = "http://" + ATLAS_DOMAIN + ":" + ATLAS_PORT + restAPI
    print ("curl -d @entity.json -X POST -H \"Content-Type: application/json\" %s" % (url))
    r = requests.post(url, auth=("admin", "admin"),json=postData)

    jsonResult = {
        "statusCode": r.status_code,
        "msg": r.text,
        "postData" :  postData
    }
    if (r.status_code == 200):
       jsonResult = json.loads(r.text)

    return (jsonResult);


def rangerGET( restAPI ) :
    url = "http://"+RANGER_DOMAIN+":"+RANGER_PORT+restAPI
    r= requests.get(url, auth=("admin", "admin"))
    return(json.loads(r.text));

def rangerPOST( restAPI, rangerData) :
    url = "http://" + RANGER_DOMAIN + ":" + RANGER_PORT + restAPI
    r = requests.post(url, auth=("admin", "admin"),json=rangerData)
    return (json.loads(r.text));


def rangerPUT( restAPI, rangerData) :
    url = "http://" + RANGER_DOMAIN + ":" + RANGER_PORT + restAPI
    r = requests.put(url, auth=("admin", "admin"),json=rangerData)
    return (json.loads(r.text));


def rangerDELETE( restAPI) :
    url = "http://" + RANGER_DOMAIN + ":" + RANGER_PORT + restAPI
    r = requests.delete(url, auth=("admin", "admin"))
    return (json.loads(r.text));


