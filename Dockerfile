FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN python -m pip install -r requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

#CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", "0.0.0.0:8000", "--chdir", "biblioteca", "wsgi:application"]
