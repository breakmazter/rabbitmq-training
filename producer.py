import pika
from settings import *


def main():
    credentials = pika.PlainCredentials(RABBITMQ_LOGIN, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, virtual_host=RABBITMQ_VHOST, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='mazan_green_queue', durable=True)

    message = input("Write coeff : ")
    channel.basic_publish(exchange='', routing_key='mazan_green_queue', body=message,
                          properties=pika.BasicProperties(delivery_mode=2, ))
    print("[Producer] sent %r" % (message,))
    connection.close()


if __name__ == "__main__":
    main()