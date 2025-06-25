FROM python:3.13.5-slim

RUN mkdir -p /mnt/data
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY counter-service.py ./

EXPOSE 80
CMD [ "python", "./counter-service.py"]