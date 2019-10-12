FROM python:3.7.3-alpine
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
COPY . /flask-template
WORKDIR /flask-template
CMD ["supervisord", "-c", "supervisor/supervisord.conf"]