import boto3
import pymysql

REGION = 'us-east-1'
rds_host = "cacaodatabase.cfsj3g78c3hc.us-east-1.rds.amazonaws.com"
name = "admin"
password = ""
db_name = "cacao"
conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

sns = boto3.client("sns",
                   aws_access_key_id="",
                   aws_secret_access_key="",
                   region_name="us-east-1"
                   )

brand_list = {"starbucks": "스타벅스", "hollys": "할리스", "tomntoms": "탐앤탐스", "ediya": "이디야", \
              "coffeebean": "커피빈", "twosome": "투썸플레이스", "angelinus": "엔제리너스", "paikdabang": "빽다방"}

def lambda_handler(event, context):
    for record in event['Records']:
        brand = record['s3']['object']['key'].split('_')[0]
        # brand = record['s3']['bucket']['name'].split('-')[1]
        with conn.cursor() as cur:
            cur.execute("select name, phone_number, brand from userinfo where brand = '" + brand + "'")
            conn.commit()
            for row in cur.fetchall():
                print(row[1])
                print(brand_list[brand])
                sns.publish(Message=brand_list[brand]+"에서 새로운 메뉴가 출시되었습니다! www.caca0.shop에서 지금 바로 만나보세요!", PhoneNumber=row[1])
            cur.close()
