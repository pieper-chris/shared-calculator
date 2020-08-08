web: daphne pycalc.pycalc.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python pycalc/manage.py runworker --only-channels=http.* --only-channels=websocket.* -v2