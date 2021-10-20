FROM python:3.7
WORKDIR /analytics

# Install Requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Add Postgres client
RUN apt-get update -y && \
    apt-get install libpq-dev python3-dev -y && \
    pip3 install psycopg2==2.8.6

EXPOSE 8000
EXPOSE 8052

CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']