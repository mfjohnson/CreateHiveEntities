from ATLASAPI import *

DB_NAME = "TEST_DB"

print("The 'hive_db' Atlas Type")
print("========================")
hive_db = atlasREST("/api/atlas/types/hive_db")
print json.dumps(hive_db, indent=2, sort_keys=True)


hive_db_entity = {
    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
    "id": {
        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
        "id": "-1234",
        "typeName": "hive_db",
        "state": "ACTIVE"
    },
    "typeName": "hive_db",
    "values": {
        "name": DB_NAME,
        "location": "ABC",
        "qualifiedName": "TEST_DB@HDP",
        "clusterName": "HDP"
    },
    "traitNames": [

    ],
    "traits": {
    }
}

print("-------------------------")
print("  The new hive_db entity definition")
print("========================")
hive_db_json = json.dumps(hive_db_entity)
print json.dumps(hive_db_entity, indent=2, sort_keys=True)
print("-------------------------")
print("  New hive_db create result")
print("========================")
result = atlasPOST("/api/atlas/entities", hive_db_json)
print json.dumps(result, indent=2, sort_keys=True)
