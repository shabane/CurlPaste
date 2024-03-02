#!/usr/bin/env python3
import sqlite3
from datetime import datetime, timedelta
import os
import time


def remove_file(path: str):
    os.remove(path)

def remove_from_db(db, id: int):
    cursor = db.cursor()
    cursor.execute(f"DELETE from paste_file where id = {id}")
    cursor.execute(f"DELETE from paste_limit where id = {id}")
    db.commit()

while True:
    db = sqlite3.connect('db.sqlite3')
    # id, view, time, file
    limits = db.execute('select * from paste_limit').fetchmany()

    # id, name, file, date_time, visited, password
    files = db.execute('select * from paste_file').fetchmany()

    for file, limit in zip(files, limits):
        _file_time = file[3]
        _file_time = datetime.strptime(_file_time, "%Y-%m-%d %H:%M:%S.%f")
        _limit_hour = limit[2]

        _visit_limit = limit[1]
        _file_visited = file[4]

        if datetime.now() >= _file_time+timedelta(hours=_limit_hour):
            remove_file(f'./media/{file[2]}')
            remove_from_db(db, file[0])
            print(file)

        if _visit_limit and _file_visited >= _visit_limit:
            remove_file(f'./media/{file[2]}')
            remove_from_db(db, file[0])
            print(file)
        time.sleep(0.25)
