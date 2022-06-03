FROM python:3.9
WORKDIR /Project/

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/


COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]%