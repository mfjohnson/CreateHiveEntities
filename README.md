# Overview
A series of ATLAS REST examples to create Atlas Hive Entities

Types of hive Atlas entities covered in this Article:

| Atlas Entity | Description |
|--------------|-------------|
| hive_db      | Defines a Hive DATABASE entity. |
| hive_table   | Defines a Hive TABLE entity. |

# Requirements
All of the examples within this project were built using:
- HDP 2.5.0 (later versions with Atlas 0.7 or greater hopefully should also work)
- Python 2.7 (curl examples will also be presented in the Article)
- PySpark for creating Hive_table entities concurrently

# Configuring the Examples for your environment

- You will need to specify the Atlas FQDN and Port from your cluster in the file ATLASAPI.py
 
 | Variable to change | Currently Set to |Description |
 |--------------------|------------------|------------|
 |ATLAS_DOMAIN        | server1          | The Atlas UI server FQDN.  If uncertain, go to Ambari and select the Atlas service and then from the summary tag, click 'Atlas Metadata Server'.  That will be your Atlas Domain value|
 |ATLAS_PORT          | 21000            | In most sites the port will default to 21000.  If you are having port problems, then check out the property 'atlas.server.http.port' |
 | NAMENODE_PRIMARY | server1.hdp | The HDFS Namenode primary server FQDN.  If uncertain, go to Ambari and select HDFS and then the summary tag.  From there click 'Namenode' to determine your server name.  |
 | NAMENODE_PORT | 8020 | The default namenode primary server port. |
 | CLUSTERNAME | HDP | The name of the cluster to connect.  The name should appear just to the right of the Ambari logo |

# Test Entity Create Examples
## Create a Hive DB Entity

In this example we will create a 'hive_db' entity named 'TEST_DB' using the Atlas Rest API.  

## Create a Hive Table Entity
## Create Multiple Hive Table Entities
## Create Multiple Hive Table Entities using PySpark
## Add Column to Hive Table Entity

# Bibliography
