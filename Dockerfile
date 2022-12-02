FROM python:3.8-alpine

WORKDIR /app/
ADD ./platform /app/platform/
ADD ./bin /app/bin/
ADD ./requirements.txt  /app/requirements.txt

RUN pip install -U pip
RUN pip install -r /app/requirements.txt

RUN chmod +x /app/bin/platform_start.sh
CMD [ "sh","/app/bin/platform_start.sh"]
