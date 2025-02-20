FROM python:3.9-alpine 
WORKDIR /rcontrol
RUN pip install --upgrade pip
ADD . /rcontrol
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
