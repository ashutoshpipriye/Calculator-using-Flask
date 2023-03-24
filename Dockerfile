From python:3.10
Copy . /app
Workdir /app
Run apt-get update
Run pip install flask
ENV FLASK_APP=calc.py
Expose 5000
Cmd [ "flask","run","--host=0.0.0.0" ]
