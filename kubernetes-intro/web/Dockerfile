FROM python:3.8

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

RUN chown -R 1001 /app
USER 1001

CMD ["gunicorn", "--bind", "127.0.0.1:8000", "app:app"]
