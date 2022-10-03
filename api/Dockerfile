FROM python:3.9.14

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT python3 manage.py runserver