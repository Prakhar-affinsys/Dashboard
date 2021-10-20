FROM python:3.7
WORKDIR /analytics

COPY requirements.txt /analytics
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install /analytics/requirements.txt

# Add Postgres client
RUN apt-get update -y && \
    apt-get install libpq-dev python3-dev -y && \
    pip3 install psycopg2==2.8.6

EXPOSE 8000
EXPOSE 8052

CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']