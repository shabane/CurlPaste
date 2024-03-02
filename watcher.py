#!/usr/bin/env python3
import sqlite3
from datetime import datetime, timedelta


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
        print('yay its worked!')

    if _visit_limit and _file_visited >= _visit_limit:
        ...
