FROM python:3.9.14

WORKDIR /app

# RUN sudo apt-get install build-dep python-psycopg2
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT python3 main.py