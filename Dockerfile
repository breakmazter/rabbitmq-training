FROM python:3.9-alpine

COPY consumer.py /work/
COPY settings.py /work/

RUN pip install requirements.txt

WORKDIR /work/

CMD ["python", "consumer.py"]

