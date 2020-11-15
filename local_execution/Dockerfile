FROM python:3.6

WORKDIR /workspace/project

RUN mkdir -p /opt/bitnami/python/bin && \
    ln -s /usr/bin/python3.6 /opt/bitnami/python/bin/python3.6

ENV PYSPARK_PYTHON=/opt/bitnami/python/bin/python3.6

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install default-jdk-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

COPY src/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

COPY entrypoint-jupyter.sh /entrypoint-jupyter.sh
RUN chmod +x /entrypoint-jupyter.sh
EXPOSE 8888

CMD ["/entrypoint-jupyter.sh"]
