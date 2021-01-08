FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1419382865395-1486954156113-96vYGSc81f3AgpuQ2TodZ7Vy"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
