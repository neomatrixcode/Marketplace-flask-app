#!/bin/bash
bash /app/prestart.sh
#python3 app.py
nginx && uwsgi --ini /app.ini
