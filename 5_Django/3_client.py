"""
https://www.pythonanywhere.com/user/kevinstevens/
console > bash
mkvirtualenv django3 --python=/usr/bin/python3.6
pip install django
workon django3
python -m django --version
cd ~
git clone https://github.com/csev/dj4e-samples
cd dj4e-samples/
pip install -r requirements.txt
python manage.py check
python manage.py makemigrations
python manage.py migrate
cd ~
mkdir django_projects
cd django_projects
django-admin startproject mysite
vi ~/django_projects/mysite/mysite/settings.py
ALLOWED HOSTS = ['*']
python manage.py check
"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=' ')

mysock.close()

