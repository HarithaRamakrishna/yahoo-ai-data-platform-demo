{{config(materialized = 'table')}}

with events AS(
    select user_id,
    count(*) as total_events,
    count(distinct session_id) as sessions,
    max(timestamp) as last_event_ts 
    from {{ref('clickstream')}}
    group by user_id
),

users AS(
    select 
        user_id,
        signup_ts,
        region,
        device,
        referrer
    from {{ref'users'}}
)

select 
    u.user_id,
    u.region,
    u.device,
    u.referrer,
    events.total_events,
    events.sessions,
    events.last_event_ts,
    DATEDIFF(current_date, DATE(u.signup_ts), DAY) as days_active
from users u
left join events ON u.user_id = events.user_id