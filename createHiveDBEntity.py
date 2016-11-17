from ATLASAPI import *

DB_NAME="TEST_DB"

hive_db_entity = {
  "version": {
    "version": "1.0.0"
  },
  "message": {
    "entities": [
      {
        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
        "id": {
          "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
          "id": "-712321076869990",
          "version": 0,
          "typeName": "hive_db",
          "state": "ACTIVE"
        },
        "typeName": "hive_db",
        "values": {
          "name": DB_NAME,
          "location": "hdfs://server1.hdp:8020/apps/hive/warehouse",
          "description": "Default Hive database",
          "ownerType": 2,
          "qualifiedName": "%s@HDP" % (DB_NAME),
          "owner": "public",
          "clusterName": "HDP",
          "parameters": {}
        },
        "traitNames": [],
        "traits": {}
      }
    ]
  }
}
payload = {'key1': 'value1', 'key2': 'value2'}
hive_db_json = json.dumps(hive_db_entity)
result = atlasPOST("/v1/entities", hive_db_json)
print json.dumps(result, indent=2, sort_keys=True)
