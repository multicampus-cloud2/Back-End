import pymysql
# import sys

REGION = 'us-east-1'

rds_host  = "cacaodatabase.cfsj3g78c3hc.us-east-1.rds.amazonaws.com"
name = "admin"
password = "cacaoproject"
db_name = "cacao"

def lambda_handler(event, context):
    
    result = []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    with conn.cursor() as cur:
        cur.execute("select size from hollys")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print ("Data from RDS...")
        print (result)
    return result

# def main(event, context):
#     save_events(event)