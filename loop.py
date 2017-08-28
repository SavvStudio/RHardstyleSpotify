import datetime

def run_function_every_monday(loopedFunction):
    last_run = datetime.datetime.fromtimestamp(0)

    while True:
        today = datetime.datetime.today()
        if(datetime_is_monday(today) and last_run.date() != today.date()):
            loopedFunction()
            last_run = today

def datetime_is_monday(date_time):
    return date_time.today().weekday() == 0