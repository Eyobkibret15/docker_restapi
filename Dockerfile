FROM python:alpine3.14

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh
CMD ["python3", "manage.py" "collectstatic" "--no-input"]
CMD ["python3", "manage.py" "makemigrations"]
CMD ["python3", "manage.py" "migrate" "--no-input"]
# ENTRYPOINT ["/app/entrypoint.sh"]
