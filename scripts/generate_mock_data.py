import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
Faker.seed(42)

#Create two csv files
users_file = 'data/users.csv'
clickstream_file = 'data/clickstream.csv'

regions = ['US', 'IN','CA','UK','AU']
devices = ['mobile','desktop','tablet']
referrers = ['google','email','social','direct','affliate']

user_ids = []

with open(users_file, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['user_id', 'signup_ts', 'region', 'device', 'referrer'])

    for i in range(1,201):
        user_id = 1000 + i
        signup_ts = fake.date_between(start_date = '-2y', end_date = '-1d')
        region = random.choice(regions)
        device = random.choice(devices)
        referrer = random.choice(referrers)
        writer.writerow([user_id, signup_ts,region,device,referrer])
        user_ids.append(user_id)
        
print(f" Generated {users_file}")

#Create the clickstream file clickstream.csv
event_types = ['click', 'scroll','hover']
pages = ['/home','/news','/sports','/finance','/entertainment']

with open(clickstream_file, mode = 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['event_id','user_id','timestamp', 'page','event_type','session_id'])
    for i in range(1,1001):
        eid = f"e{i:05}"
        uid = random.choice(user_ids)
        ts = fake.date_time_between(start_date = '-1y', end_date = 'now')
        page = random.choice(pages)
        etype = random.choice(event_types)
        sess = f"sess_{random.randint(100,999)}"
        writer.writerow([eid,uid,ts,page,etype,sess])
print(f" Generated {clickstream_file}")
