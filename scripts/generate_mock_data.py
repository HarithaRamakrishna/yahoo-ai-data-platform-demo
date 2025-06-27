import csv
import random
from faker import Faker

# File paths (module‐level so tests can import them)
users_file = 'data/users.csv'
clickstream_file = 'data/clickstream.csv'

def main():
    fake = Faker()
    Faker.seed(42)
    random.seed(42)

    regions   = ['US', 'IN', 'CA', 'UK', 'AU']
    devices   = ['mobile', 'desktop', 'tablet']
    referrers = ['google', 'email', 'social', 'direct', 'affiliate']

    user_ids = []

       #1) Generate users.csv
    with open(users_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'signup_ts', 'region', 'device', 'referrer'])
        for i in range(1, 201):
            user_id   = 1000 + i
            signup_ts = fake.date_between(start_date='-2y', end_date='-1d')
            region    = random.choice(regions)
            device    = random.choice(devices)
            referrer  = random.choice(referrers)
            writer.writerow([user_id, signup_ts, region, device, referrer])
            user_ids.append(user_id)
    print(f"Generated {users_file}")

    # 2) Generate clickstream.csv
    event_types = ['click', 'scroll', 'hover']
    pages       = ['/home', '/news', '/sports', '/finance', '/entertainment']

    with open(clickstream_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['event_id', 'user_id', 'timestamp', 'page', 'event_type', 'session_id'])
        for i in range(1, 1001):
            event_id   = f"e{i:05}"
            uid        = random.choice(user_ids)
            timestamp  = fake.date_time_between(start_date='-1y', end_date='now')
            page       = random.choice(pages)
            event_type = random.choice(event_types)
            session_id = f"sess_{random.randint(100,999)}"
            writer.writerow([event_id, uid, timestamp, page, event_type, session_id])
    print(f"Generated {clickstream_file}")

if __name__ == "_main_":
    main()