import tweepy
from datetime import datetime, timezone, timedelta
import os

# --- CONFIGURATION ---
# Release Date: November 6, 2026
# We set the time to 00:00 IST (Indian Standard Time)
IST_OFFSET = timedelta(hours=5, minutes=30)
TARGET_DATE = datetime(2026, 11, 6, 0, 0, 0, tzinfo=timezone(IST_OFFSET))

EVENT_NAME = "Ramayana"
HASHTAGS = "#Ramayana #RanbirKapoor #NiteshTiwari #NamitMalhotra"

def create_tweet():
    # 1. Authenticate to X
    client = tweepy.Client(
        consumer_key=os.environ['API_KEY'],
        consumer_secret=os.environ['API_SECRET'],
        access_token=os.environ['ACCESS_TOKEN'],
        access_token_secret=os.environ['ACCESS_SECRET']
    )

    # 2. Calculate Days Remaining (Relative to IST)
    # Get current time in UTC, then convert to IST
    now_utc = datetime.now(timezone.utc)
    now_ist = now_utc.astimezone(timezone(IST_OFFSET))
    
    # Calculate difference
    difference = TARGET_DATE - now_ist
    days_left = difference.days + 1  # Add 1 to count the current partial day

    # 3. Logic
    if days_left > 0:
        text = f"Only {days_left} days left until {EVENT_NAME}! 🏹⏳\n\n{HASHTAGS}"
    elif days_left == 0:
        text = f"TODAY IS THE DAY! {EVENT_NAME} releases today! 🏹🔥\n\n{HASHTAGS}"
    else:
        print("Event has passed.")
        return

    # 4. Post the Tweet
    try:
        response = client.create_tweet(text=text)
        print(f"Tweet posted! ID: {response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    create_tweet()
    create_tweet()
