FROM python:3.5

COPY . /opt/django/sofiart
COPY sofiart_nginx.conf /etc/nginx/sites-available/
WORKDIR /opt/django/sofiart

RUN apt update && \
    apt install nginx -y && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir /var/uwsgi/ && chmod 777 /var/uwsgi/ && \
    ln -s /etc/nginx/sites-available/sofiart_nginx.conf /etc/nginx/sites-enabled


EXPOSE 8000 80
CMD python manage.py makemigrations && \
    python manage.py migrate && \
    service nginx start --uid www && \
    uwsgi sofiart_uwsgi.ini
