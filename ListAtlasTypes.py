from ATLASAPI import *

types = atlasREST("/api/atlas/types/hive_db")
print json.dumps(types, indent=2, sort_keys=True)

