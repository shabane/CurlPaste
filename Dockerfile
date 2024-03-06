FROM ubuntu:latest
RUN apt-get update && apt-get install nginx python3 python3-pip gunicorn -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "/bin/sh", "-c", "/app/main.sh" ]