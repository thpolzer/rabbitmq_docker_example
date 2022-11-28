FROM python:3.8

# set workind directory
WORKDIR /home
# set arg
ENV SERVERNAME localhost
# copy code to container
ADD  producer.py /home/
# install RabbitMQ client
RUN pip install pika
# start command
CMD [ "python", "producer.py"]
