
FROM  python:3.8-rc-slim-buster

ADD main.py
    docker build -t getting-started .
RUN pip install requests requirements.txt

CMD ["python:3","./main.py"]




