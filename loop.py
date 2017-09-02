import datetime
import database

def run_function_every_monday(loopedFunction):
    last_run = database.get_latest_run()

    while True:
        today = datetime.datetime.today()
        if(datetime_is_monday(today) and last_run.date() != today.date()):
            loopedFunction()

def datetime_is_monday(date_time):
    return date_time.today().weekday() == 0