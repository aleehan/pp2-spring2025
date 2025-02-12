from datetime import datetime

def drop_microseconds():
    current_time = datetime.now()
    without_microsuconds = current_time.replace(microsecond=0)
    print(f"Current time: {current_time}\nWithout microseconds: {without_microsuconds}")

drop_microseconds()