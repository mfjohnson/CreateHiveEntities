from ATLASAPI import *
import json

DB_NAME = "TEST_DB"
results = atlasREST("/api/atlas/types/hive_db")
print json.dumps(results, indent=2, sort_keys=True)

hive_table_def = {
    {
        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
        "id": {
            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
            "id": "-712321076869990",
            "typeName": "hive_db",
        },
        "typeName": "hive_db",
        "values": {
            "name": "default",
            "location": "hdfs://server1.hdp:8020/apps/hive/warehouse",
            "description": "Default Hive database",
            "ownerType": 2,
            "qualifiedName": "default@HDP",
            "owner": "public",
            "clusterName": "HDP",
            "parameters": {}
        },
        "traitNames": [],
        "traits": {}
    },
    {
        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
        "id": {
            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
            "id": "-712321076869989",
            "version": 0,
            "typeName": "hive_table",
            "state": "ACTIVE"
        },
        "typeName": "hive_table",
        "values": {
            "tableType": "MANAGED_TABLE",
            "name": "stocks",
            "createTime": "2016-11-01T12:16:31.000Z",
            "temporary": False,
            "db": {
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
                    "name": "default",
                    "location": "hdfs://server1.hdp:8020/apps/hive/warehouse",
                    "description": "Default Hive database",
                    "ownerType": 2,
                    "qualifiedName": "default@HDP",
                    "owner": "public",
                    "clusterName": "HDP",
                    "parameters": {}
                },
                "traitNames": [],
                "traits": {}
            },
            "retention": 0,
            "qualifiedName": "default.stocks@HDP",
            "columns": [
                {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                    "id": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869987",
                        "version": 0,
                        "typeName": "hive_column",
                        "state": "ACTIVE"
                    },
                    "typeName": "hive_column",
                    "values": {
                        "name": "transdte",
                        "qualifiedName": "default.stocks.transdte@HDP",
                        "owner": "demo1",
                        "type": "string",
                        "table": {
                            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                            "id": "-712321076869989",
                            "version": 0,
                            "typeName": "hive_table",
                            "state": "ACTIVE"
                        }
                    },
                    "traitNames": [],
                    "traits": {}
                },
                {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                    "id": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869986",
                        "version": 0,
                        "typeName": "hive_column",
                        "state": "ACTIVE"
                    },
                    "typeName": "hive_column",
                    "values": {
                        "name": "open_price",
                        "qualifiedName": "default.stocks.open_price@HDP",
                        "owner": "demo1",
                        "type": "float",
                        "table": {
                            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                            "id": "-712321076869989",
                            "version": 0,
                            "typeName": "hive_table",
                            "state": "ACTIVE"
                        }
                    },
                    "traitNames": [],
                    "traits": {}
                },
                {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                    "id": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869985",
                        "version": 0,
                        "typeName": "hive_column",
                        "state": "ACTIVE"
                    },
                    "typeName": "hive_column",
                    "values": {
                        "name": "high_price",
                        "qualifiedName": "default.stocks.high_price@HDP",
                        "owner": "demo1",
                        "type": "float",
                        "table": {
                            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                            "id": "-712321076869989",
                            "version": 0,
                            "typeName": "hive_table",
                            "state": "ACTIVE"
                        }
                    },
                    "traitNames": [],
                    "traits": {}
                },
                {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                    "id": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869984",
                        "version": 0,
                        "typeName": "hive_column",
                        "state": "ACTIVE"
                    },
                    "typeName": "hive_column",
                    "values": {
                        "name": "low_price",
                        "qualifiedName": "default.stocks.low_price@HDP",
                        "owner": "demo1",
                        "type": "float",
                        "table": {
                            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                            "id": "-712321076869989",
                            "version": 0,
                            "typeName": "hive_table",
                            "state": "ACTIVE"
                        }
                    },
                    "traitNames": [],
                    "traits": {}
                },
                {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                    "id": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869983",
                        "version": 0,
                        "typeName": "hive_column",
                        "state": "ACTIVE"
                    },
                    "typeName": "hive_column",
                    "values": {
                        "name": "close_price",
                        "qualifiedName": "default.stocks.close_price@HDP",
                        "owner": "demo1",
                        "type": "float",
                        "table": {
                            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                            "id": "-712321076869989",
                            "version": 0,
                            "typeName": "hive_table",
                            "state": "ACTIVE"
                        }
                    },
                    "traitNames": [],
                    "traits": {}
                },
                {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                    "id": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869982",
                        "version": 0,
                        "typeName": "hive_column",
                        "state": "ACTIVE"
                    },
                    "typeName": "hive_column",
                    "values": {
                        "name": "volume",
                        "qualifiedName": "default.stocks.volume@HDP",
                        "owner": "demo1",
                        "type": "int",
                        "table": {
                            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                            "id": "-712321076869989",
                            "version": 0,
                            "typeName": "hive_table",
                            "state": "ACTIVE"
                        }
                    },
                    "traitNames": [],
                    "traits": {}
                },
                {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                    "id": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869981",
                        "version": 0,
                        "typeName": "hive_column",
                        "state": "ACTIVE"
                    },
                    "typeName": "hive_column",
                    "values": {
                        "name": "adj_price",
                        "qualifiedName": "default.stocks.adj_price@HDP",
                        "owner": "demo1",
                        "type": "float",
                        "table": {
                            "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                            "id": "-712321076869989",
                            "version": 0,
                            "typeName": "hive_table",
                            "state": "ACTIVE"
                        }
                    },
                    "traitNames": [],
                    "traits": {}
                }
            ],
            "lastAccessTime": "2016-11-01T12:16:31.000Z",
            "owner": "demo1",
            "sd": {
                "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Reference",
                "id": {
                    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                    "id": "-712321076869988",
                    "version": 0,
                    "typeName": "hive_storagedesc",
                    "state": "ACTIVE"
                },
                "typeName": "hive_storagedesc",
                "values": {
                    "location": "hdfs://server1.hdp:8020/apps/hive/warehouse/stocks",
                    "serdeInfo": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Struct",
                        "typeName": "hive_serde",
                        "values": {
                            "serializationLib": "org.apache.hadoop.hive.ql.io.orc.OrcSerde",
                            "parameters": {
                                "serialization.format": "1"
                            }
                        }
                    },
                    "qualifiedName": "default.stocks@HDP_storage",
                    "outputFormat": "org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat",
                    "compressed": False,
                    "numBuckets": -1,
                    "inputFormat": "org.apache.hadoop.hive.ql.io.orc.OrcInputFormat",
                    "parameters": {},
                    "storedAsSubDirectories": False,
                    "table": {
                        "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_Id",
                        "id": "-712321076869989",
                        "version": 0,
                        "typeName": "hive_table",
                        "state": "ACTIVE"
                    }
                },
                "traitNames": [],
                "traits": {}
            },
            "parameters": {
                "rawDataSize": "0",
                "numFiles": "0",
                "transient_lastDdlTime": "1478002591",
                "totalSize": "0",
                "COLUMN_STATS_ACCURATE": "{\"BASIC_STATS\":\"true\"}",
                "numRows": "0"
            },
            "partitionKeys": []
        },
        "traits": {}
    }
}
result = atlasPOST("/api/atlas/entities", json.dumps(hive_table_def))
print json.dumps(result, indent=2, sort_keys=True)
