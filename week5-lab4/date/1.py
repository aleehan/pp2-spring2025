from datetime import datetime, timedelta

def difference():
    today = datetime.now()
    dif = today - timedelta(days = 5)
    print (dif.strftime("%d-%m-%Y"))

difference()