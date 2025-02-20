FROM python:3.9-alpine 
WORKDIR /webapp
RUN pip install --upgrade pip
ADD . /webapp
RUN pip install --no-cache-dir -r requirements.txt
# gunicorn --preload --timeout 120 --bind=0.0.0.0:8001 --workers=3 --worker-class gevent --log-level DEBUG app:app 
CMD ["gunicorn", "--preload", "--timeout", "120", "--bind", "0.0.0.0:8001", "--log-level", "DEBUG", "app:app"]
