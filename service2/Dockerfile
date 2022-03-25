FROM python:latest
COPY . .
RUN pip install -r requirements.txt
EXPOSE ?
ENTRYPOINT ["python", "app.py"]