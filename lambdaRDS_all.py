# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys
import json

REGION = 'us-east-1'

rds_host  = "cacaodatabase.cfsj3g78c3hc.us-east-1.rds.amazonaws.com"
name = "admin"
password = "cacaoproject"
db_name = "cacao"

def lambda_handler(event, context):
    
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    brand_list = ["starbucks", "hollys", "tomntoms", "ediya", "coffebean", "twosome", "angelinus",  "paikdabang"]
    json_data = []
    idx = 1
    
    for brand in brand_list:
        with conn.cursor() as cur:
            cur.execute("select * from " + brand)
            conn.commit()
            cur.close()
    
            keys = []
            for column in cur.description:
                keys.append(column[0])
                key_number = len(keys)
    
            for row in cur.fetchall():
                item = dict()
                item['brand'] = brand.capitalize()
                for q in range(key_number):
                    item[keys[q]] = row[q]
                json_data.append(item)
            
    return json_data

def main(event, context):
    save_events(event)