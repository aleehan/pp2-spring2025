from datetime import datetime, timedelta

def triple_days():
    today = datetime.now()
    yesteday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print(f"yesterday: {yesteday.strftime("%d-%m-%Y")}\ntoday: {today.strftime("%d-%m-%Y")}\ntomorrow: {tomorrow.strftime("%d-%m-%Y")}")

triple_days()