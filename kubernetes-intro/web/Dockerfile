FROM python:3.8

ENV DIRECTORY=/app
ENV PORT=8000
ENV USER=1001

EXPOSE ${PORT}

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR ${DIRECTORY}
ADD . ${DIRECTORY}

RUN chown -R ${USER} ${DIRECTORY}
USER ${USER}

CMD ["python", "app.py"]
