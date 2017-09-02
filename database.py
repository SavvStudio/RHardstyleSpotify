import sqlite3
import datetime

def log_run():
    database = sqlite3.connect("rhard.db")
    cursor = database.cursor()
    today = datetime.datetime.today()
    cursor.execute("INSERT INTO runs (date) VALUES (?)", (today,))
    database.commit()
    database.close()

def get_latest_run():
    database = sqlite3.connect("rhard.db")
    cursor = cursor = database.cursor()
    cursor.execute("SELECT date FROM runs ORDER BY date DESC LIMIT 1")
    results = cursor.fetchone()

    latest_run_date = datetime.datetime.fromtimestamp(0)
    if(results != None):
        latest_run_date = datetime.datetime.strptime(results[0], '%Y-%m-%d %H:%M:%S.%f')

    return latest_run_date