FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1419382865395-1486954156113-wM5nTYBdlIQSUxhbut8LKLLo"
ENV SLACK_SIGNING_SECRET="8498970ebf81815062f935ff1ce8fb9b"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader

COPY ./nestor_slack_reader.py /nestor_slack_reader.py

CMD [ "python", "/nestor_slack_reader.py" ]
