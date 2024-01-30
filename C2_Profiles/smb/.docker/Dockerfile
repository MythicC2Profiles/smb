FROM python:3.11-slim

COPY [".docker/requirements.txt", "requirements.txt"]
RUN pip install --no-cache -r requirements.txt

WORKDIR /Mythic/
COPY [".", "."]
CMD ["python3", "main.py"]