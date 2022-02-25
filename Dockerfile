FROM python:3.10

WORKDIR ./EMIS_Project

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY ./ ./

CMD ["python", "./main.py"]


