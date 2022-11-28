# rabbitmq_docker_example

Das in diesem Prokjekt implementierte Beispiel ist in Python implementiert und verwendet die Python-Version **3.8**.  
Als zusätzliche Python-Library ist der RabbitMQ-Client **pika** zu implementieren: *pip install pika*

Das zugrundeliegende Setup geht von 3 Containern aus:
- RabbitMQ-Broker
- RabbitMQ-Producer-Client
- RabbitMQ-Consumer-Client

### 1. Container-Netzwerk
Damit die drei Container miteinander kommunizieren können, müssen diese auf einem gemeinsamen Docker-Netzwerk laufen.  
Hierzu ist ein separates Docker-Netzwerk mit einem IP-Adressen-Bereich anzulegen, etwa mittels  
*docker network create --subnet=172.18.0.0/24 static-network-rabbitmq*  
Mit dem Befehl *docker network ls* kann man überprüfen, ob das Netzwerk korrekt angelegt wurde.

### 2. Starten des RabbitMQ-Brokers
siehe hierzu https://www.rabbitmq.com/download.html  
*docker run -it --rm --name rabbitmq_broker -h rabbitmq_broker --net static-network-rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management*

Dem oben stehenden RabbitMQ-Broker wird mit dem Parameter *h* ein Hostname zugewiesen. Dieser wird dann beim Producer und Consumer als Umgebungsvariable verwendet, um die Verbindung zum Broker aufzubauen.

Auf die Admin-Konsole kann im Browser mit folgender URL zugegriffen werden:  
http://localhost:15672/

- Username: guest
- Password: guest

### 3. RabbitMQ-Producer
- 3.1 Build  
*docker build -t polzer/rabbitmq_producer:v02 .*  
- 3.2 Starten des Containers  
*docker run -it --name producer -e SERVERNAME=rabbitmq_broker --net static-network-rabbitmq polzer/rabbitmq_producer:v02*  

### 4. RabbitMQ-Consumer
- 4.1 Build  
*docker build -t polzer/rabbitmq_consumer:v02 .*  
- 4.2 Starten des Containers  
*docker run -it --name consumer -e SERVERNAME=rabbitmq_broker --net static-network-rabbitmq polzer/rabbitmq_consumer:v02*  
