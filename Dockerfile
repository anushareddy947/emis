
FROM  python:3.8-rc-slim-buster

ADD main.py

RUN pip install requests requirements.txt

CMD ["python:3","./main.py"]




