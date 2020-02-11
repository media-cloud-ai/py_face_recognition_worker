FROM mediacloudai/py_amqp_worker:latest

WORKDIR /sources

ADD . /sources

RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-dev \
        python3-pip && \
    pip3 install .


ENV PYTHONPATH=/sources
ENV PYTHON_WORKER_FILENAME=/sources/worker.py
ENV AMQP_QUEUE=job_face_recognition_processing

CMD py_amqp_worker
