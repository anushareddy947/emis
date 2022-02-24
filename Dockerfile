# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install requirements.txt
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "main.py"]

