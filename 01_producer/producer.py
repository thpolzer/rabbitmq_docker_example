import pika, json, os

#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
servername = os.getenv('SERVERNAME')
connection = pika.BlockingConnection(pika.ConnectionParameters(servername))
channel = connection.channel()

channel.queue_declare(queue='test')

msg = {"mymessages" : [{"id":1,"name":"Thomas"},{"id":2,"name":"Lina"}]}
message = json.dumps(msg)

channel.basic_publish(exchange='',
                      routing_key='test',
                      body=message)
print(" [x] Sent JSON data!")

#connection.close()
