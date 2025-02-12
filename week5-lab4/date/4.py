from datetime import datetime, timedelta

def difference_in_seconds(date1str, date2str):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date1str, date_format)
    date2 = datetime.strptime(date2str, date_format)

    result = abs(date1 - date2)
    result_in_seconds = result.total_seconds()
    print(f"The difference in seconds: {result_in_seconds}")

a = input("Write the 1st date(YYYY-MM-DD): ")
b = input("Write the 2nd date(YYYY-MM-DD): ")
difference_in_seconds(a, b)