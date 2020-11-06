import pymysql
import sys
import json

REGION = 'us-east-1'

rds_host  = "cacaodatabase.cfsj3g78c3hc.us-east-1.rds.amazonaws.com"
name = "admin"
password = "cacaoproject"
db_name = "cacao"

def lambda_handler(event, context):
    brands = event['brand']
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    json_data = []
    
    with conn.cursor() as cur:
        cur.execute("select * from " + brands)
        conn.commit()
        cur.close()

        keys = []
        for column in cur.description:
            keys.append(column[0])
            key_number = len(keys)

        for row in cur.fetchall():
            item = dict()
            item['brand'] = brands
            for q in range(key_number):
                item[keys[q]] = row[q]
            json_data.append(item)
            
    return json_data