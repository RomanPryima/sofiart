FROM python:3.5

COPY . /opt/django/sofiart
COPY sofiart_nginx.conf /etc/nginx/sites-available/
WORKDIR /opt/django/sofiart

ARG SECRET_KEY
ARG RDS_DB_NAME
ARG RDS_USERNAME
ARG RDS_PASSWORD
ARG RDS_HOSTNAME
ARG RDS_PORT


ENV SECRET_KEY=$SECRET_KEY
ENV RDS_DB_NAME=$RDS_DB_NAME
ENV RDS_USERNAME=$RDS_USERNAME
ENV RDS_PASSWORD=$RDS_PASSWORD
ENV RDS_HOSTNAME=$RDS_HOSTNAME
ENV RDS_PORT=$RDS_PORT

RUN apt update && \
    apt install nginx -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir /var/uwsgi/ && chmod 777 /var/uwsgi/ && \
    ln -s /etc/nginx/sites-available/sofiart_nginx.conf /etc/nginx/sites-enabled


EXPOSE 80
CMD python manage.py makemigrations && \
    python manage.py migrate && \
    service nginx start --uid www && \
    uwsgi sofiart_uwsgi.ini
