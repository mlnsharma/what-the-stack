from cassandra.cluster import Cluster

cluster = Cluster(['db'], port=9042)
session = cluster.connect()

row = session.execute("SELECT release_version FROM system.local").one()
print(row)
if row:
    print(row[0])


