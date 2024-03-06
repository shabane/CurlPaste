#!/usr/bin/env sh

/usr/bin/python3 /app/watcher.py &

/usr/bin/gunicorn -c conf/gunicorn.conf.py curlpaste.wsgi
