import boto3
import pymysql

REGION = 'us-east-1'
rds_host = "cacaodatabase.cfsj3g78c3hc.us-east-1.rds.amazonaws.com"
name = "admin"
password = ""
db_name = "cacao"
conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

def lambda_handler(event, context):
    brand = event['brand']
    user = event['user']
    phone_number = "+82" + event['phone']

    with conn.cursor() as cur:
        cur.execute("insert into userinfo(name, phone_number, email, brand) values \
                    ('" + user['name'] + "', '" + phone_number + "', '" + user['email'] + "', '" + brand + "') \
                        on duplicate key update brand = '" + brand + "', phone_number = '" + phone_number + "'")
        conn.commit()
        cur.close()