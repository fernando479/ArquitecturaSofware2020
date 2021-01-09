FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_persistence

COPY ./persistence.py /persistence.py

CMD [ "python", "/persistence.py" ]
