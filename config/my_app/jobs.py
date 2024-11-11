# myapp/jobs.py
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from datetime import datetime
import pandas as pd

def send_scheduled_email():
    message = f'This message is suppose to sent at {hour}:{minute}'
    send_mail(
        'Message Timer',
        f'This message is suppose to sent at {hour}:{minute}',
        'akshatraj2607@gmail.com',
        ['clarkfirth72@gmail.com']
    )
    print("sent Successfully")

hour = 9
minute = 27
date_times = [
    {"date": "2024-11-07", "times": ["09:30 AM", "12:45 PM", "03:00 PM", "07:15 PM"]},
    {"date": "2024-11-08", "times": ["08:00 AM", "11:30 AM", "02:15 PM", "06:00 PM"]},
    {"date": "2024-11-09", "times": ["10:00 AM", "01:30 PM", "04:45 PM", "08:00 PM"]},
    {"date": "2024-11-10", "times": ["09:15 AM", "12:00 PM", "03:30 PM"]}
]

print(date_times)

def start():
    scheduler = BackgroundScheduler()
    df = pd.DataFrame(columns=["date", ])
    # Schedule to run daily at a specific time (e.g., 9:00 AM)
    scheduler.add_job(send_scheduled_email, 'cron', hour=hour, minute=minute)
    scheduler.start()
    
